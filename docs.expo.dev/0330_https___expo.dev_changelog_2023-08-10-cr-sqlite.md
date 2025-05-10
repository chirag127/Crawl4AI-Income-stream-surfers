---
url: https://expo.dev/changelog/2023-08-10-cr-sqlite
title: https://expo.dev/changelog/2023-08-10-cr-sqlite
date: 2025-04-30T17:18:38.448891
depth: 2
---

[All Posts](https://expo.dev/changelog)
Share this post
# [Proof of concept: expo-sqlite integration with CR-SQLite](https://expo.dev/changelog/2023-08-10-cr-sqlite)
Aug 10, 2023 by
Alan Hughes
We're releasing an alpha version of the `expo-sqlite` library that includes a proof-of-concept iOS integration with [CR-SQLite](https://github.com/vlcn-io/cr-sqlite), an SQLite extension that "allows merging different SQLite databases together that have taken independent writes" that makes up part of the [Vulcan toolchain](https://vlcn.io/).
## [Convergent, Replicated, SQLite (CR-SQLite) ](https://expo.dev/changelog/2023-08-10-cr-sqlite#convergent-replicated-sqlite-cr-sqlite)
> CR-SQLite is a [run-time loadable extension](https://www.sqlite.org/loadext.html) for [SQLite](https://www.sqlite.org/index.html) and [libSQL](https://github.com/libsql/libsql). It allows merging different SQLite databases together that have taken independent writes.With CR-SQLite, your users can all write to their own app's local SQLite database while offline. They can then come online and merge their databases together, without conflict.In other (much more technical) words, CR-SQLite adds multi-master replication and partition tolerance to SQLite via conflict-free replicated data types ([CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type)) and/or causally ordered event logs.
For more information, check out the [CR-SQLite README](https://github.com/vlcn-io/cr-sqlite).
## [Integrating expo-sqlite and CR-SQLite ](https://expo.dev/changelog/2023-08-10-cr-sqlite#integrating-expo-sqlite-and-cr-sqlite)
CR-SQLite adds functionality that allows us to request a set of changes from an SQLite database, and then we can insert those changes to another copy of the SQLite database, likely running on another device.
It works in two steps:
  * Convert tables we would like to sync to `CRRs` [(conflict-free replicated relations)](https://vlcn.io/docs/appendix/crr) with the following command:


Terminal
Copy
`SELECT crsql_as_crr('todo');`
  * Then, request the changes from the database, send them to our server, and insert them in to the receiving peer's database:


Terminal
Copy
`SELECT * FROM crsql_changes`
The results can be merged in any order (they are commutative) and the databases will always converge on the same state given the same set of operations.
## [Example project ](https://expo.dev/changelog/2023-08-10-cr-sqlite#example-project)
The example project is a todo list: [expo/todo-sync-example](https://github.com/expo/todo-sync-example/tree/initial-poc). There are two parts:
  1. **Client** : A React Native app that uses `expo-sqlite` and TinyBase to store the user's todo list.
  2. **Server** : A Node server that uses [PartyKit](https://partykit.io/) to open a websocket and listen for changes on any of the connected clients. When it receives a change, they are pushed to the other clients which will merge them into their local databases.


To run the example project, clone the [example repo](https://github.com/expo/todo-sync-example/tree/initial-poc), check out the `initial-poc` branch, and run `yarn` to install its dependencies (this project is a Yarn Classic workspace).
After that, start the server:
Terminal
Copy
`cd apps/server``yarn start`
Then, start the app:
Terminal
Copy
`cd apps/mobile``npx expo run:ios`
We now have the app running in the iOS simulator. Let's start a second instance of the app on another simulator so that we can see the sync in action:
Terminal
Copy
`npx expo run:ios -d # Select another device from the prompt`
Make some changes, add and delete todos, mark them as complete, or delete everything. No matter which device you use, you will see both stay in sync.
### [How it works ](https://expo.dev/changelog/2023-08-10-cr-sqlite#how-it-works)
The first step is to set up the TinyBase persister.
App.tsx
Copy
```

import{ useCreatePersister }from'tinybase/lib/ui-react';
import{ createExpoSqlitePersister }from'./app/store';
functionTodoList(){
// ...
useCreatePersister(
  store,
(store)=>
createExpoSqlitePersister(store, db,{
    mode:'tabular',
    tables:{
     load:{ todo:{ tableId:'todo', rowIdColumnName:'id'}},
     save:{ todo:{ tableName:'todo', rowIdColumnName:'id'}},
},
}),
[db],
async(persister)=>{
await persister.startAutoLoad();
await persister.startAutoSave();
);

```

The `createExpoSqlitePersister()` function allows TinyBase to interact with the underlying data store, which is `expo-sqlite` in this case. As we make changes to our store, changes will be persisted in the local SQLite database. This is everything we need to set up persisting our data locally.
Next, we need to notify the server of our changes. We'll use the `useSync()` hook and the `onDatabaseChange()` listener provided by `expo-sqlite`.
First, create a socket:
Code
Copy
```

// apps/mobile/app/useSync.ts
import{ useEffect, useRef }from'react';
importPartySocketfrom'partysocket';
exportfunctionuseSync(){
const socket =useRef(createPartySocket()).current;
// ...

```

Then let's connect our server:
apps/mobile/app/useSync.ts
Copy
```

exportfunctionuseSync(){
// ...
useEffect(()=>{
consthandleMessage=(e:MessageEvent<string>)=>{
if(!syncEnabled)return;
handleMessageAsync(e);
};
  socket.addEventListener('message', handleMessage);
if(syncEnabled){
// Send an init message to get the latest changes
   socket.send('init');
return()=>{
   socket.removeEventListener('message', handleMessage);
};
},[socket, syncEnabled]);
asyncfunctionhandleMessageAsync(e:MessageEvent<string>){
const data =JSON.parse(e.data);
const rows = data[0].rows;
for(const row of rows){
const{ pk,...rest }= row;
const sql =`INSERT INTO crsql_changes ("table", 'pk', 'cid', 'val', 'col_version', 'db_version', 'site_id') VALUES (?, ${pk}, ?, ?, ?, ?, ?)`;
try{
await db.execAsync(
      sql,
      args:Object.values(rest),
},
],
false
);
}catch(e){
console.log(e);

```

We register a handler for the `message` event, and when we receive it, we insert the results into our database. Finally, we use another effect to set up the `onDatabaseChange()` event listener so that we are notified when the database has changed. When we receive an update event, we request our changes from the `crsql_changes` table and send the results. Allowing enabling and disabling of the sync is optional. Also, note that the queries used here will be improved in future versions so users won't have to know about these details.
apps/mobile/app/useSync.ts
Copy
```

exportfunctionuseSync(){
// ...
useEffect(()=>{
constmaybeSendChanges=async()=>{
if(syncEnabled){
const changes =awaitrequestChanges();
    socket.send(JSON.stringify(changes));
};
// Subscribe to changes
const subscription = db.onDatabaseChange(async(result)=>{
if(result.tableName.includes('__crsql_'))return;
maybeSendChanges();
});
// Also maybe send them right away, in case changes happened while sync was
// disabled
maybeSendChanges();
return()=> subscription.remove();
},[syncEnabled]);
asyncfunctionrequestChanges(){
returnawait db.execAsync(
    sql:`SELECT "table", quote(pk) as pk, cid, val, col_version, db_version, site_id FROM crsql_changes WHERE db_version > -1`,
    args:[],
},
],
false
);

```

**Implementation note:** a real-world application would rarely want to use `WHERE db_version > -1` because this will select the entire set of changes from the `crsql_changes` table, rather than only the changes that have been applied since the most recent sync (for example: `WHERE db_version > ?last_sent_version`). We also left out `WHERE site_id IS NULL`, which is likely be used in order to ensure we only select changes that occurred on the local client, rather than re-sending changes received from a recent sync. The code is simplified here for the sake of this proof of concept, where we have not set up an state persistence on the sync server. We'll continue to iterate on the `main` branch to create an example that better represents a real app.
## [What's next ](https://expo.dev/changelog/2023-08-10-cr-sqlite#whats-next)
We plan to begin investing heavily in our SQLite bindings, `expo-sqlite`, working with [Matt Wonlaw](https://github.com/tantaman) on integrating seamlessly with CR-SQLite, and coordinating with [James Pearce](https://github.com/jamesgpearce) on a TinyBase persister. We're big believers in local-first architecture, and you should expect to see more work from us in this space in the future.
We'll continue to evolve this example to address many of the current limitations and to push more of the generic implementation details into related libraries. In particular, we plan to update it to:
  * Support the CR-SQLite extension on Android.
  * Incrementally sync changes between clients, rather than syncing the entire set of changes on each message.
  * Incrementally write to SQLite from TinyBase.
  * Demonstrate persistence on the syncing server, and examples of how you can leverage hosted SQLite services.


Send us your feedback on [Discord](https://chat.expo.dev/), [@expo](https://twitter.com/expo), [Threads](https://www.threads.net/@expo.dev), or [Bluesky](https://bsky.app/profile/expo.dev).

