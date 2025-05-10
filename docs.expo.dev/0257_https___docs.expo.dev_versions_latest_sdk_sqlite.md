---
url: https://docs.expo.dev/versions/latest/sdk/sqlite
title: https://docs.expo.dev/versions/latest/sdk/sqlite
date: 2025-04-30T17:17:28.184563
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo SQLite
A library that provides access to a database that can be queried through a SQLite API.
Android
iOS
macOS
Bundled version:
~15.1.4
`expo-sqlite` gives your app access to a database that can be queried through a SQLite API. The database is persisted across restarts of your app.
## Installation
Terminal
Copy
`- ``npx expo install expo-sqlite`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Configuration in app config
You can configure `expo-sqlite` for advanced configurations using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
### Example app.json with config plugin
app.json
Copy
```
{
 "expo": {
  "plugins": [
   [
    "expo-sqlite",
    {
     "enableFTS": true,
     "useSQLCipher": true,
     "android": {
      // Override the shared configuration for Android
      "enableFTS": false,
      "useSQLCipher": false
     },
     "ios": {
      // You can also override the shared configurations for iOS
      "customBuildFlags": ["-DSQLITE_ENABLE_DBSTAT_VTAB=1 -DSQLITE_ENABLE_SNAPSHOT=1"]
     }
    }
   ]
  ]
 }
}

Show More

```

### Configurable properties
Name| Default| Description  
---|---|---  
`customBuildFlags`| -| Custom build flags to be passed to the SQLite build process.  
`enableFTS`| `true`| Whether to enable the [FTS3, FTS4](https://www.sqlite.org/fts3.html) and [FTS5](https://www.sqlite.org/fts5.html) extensions.  
`useSQLCipher`| `false`| Use the [SQLCipher](https://www.zetetic.net/sqlcipher/) implementations rather than the default SQLite.  
## Usage
Import the module from `expo-sqlite`.
Import the module from expo-sqlite
Copy
```
import * as SQLite from 'expo-sqlite';

```

### Basic CRUD operations
Basic CRUD operations
Copy
```
const db = await SQLite.openDatabaseAsync('databaseName');
// `execAsync()` is useful for bulk queries when you want to execute altogether.
// Note that `execAsync()` does not escape parameters and may lead to SQL injection.
await db.execAsync(`
PRAGMA journal_mode = WAL;
CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY NOT NULL, value TEXT NOT NULL, intValue INTEGER);
INSERT INTO test (value, intValue) VALUES ('test1', 123);
INSERT INTO test (value, intValue) VALUES ('test2', 456);
INSERT INTO test (value, intValue) VALUES ('test3', 789);
`);
// `runAsync()` is useful when you want to execute some write operations.
const result = await db.runAsync('INSERT INTO test (value, intValue) VALUES (?, ?)', 'aaa', 100);
console.log(result.lastInsertRowId, result.changes);
await db.runAsync('UPDATE test SET intValue = ? WHERE value = ?', 999, 'aaa'); // Binding unnamed parameters from variadic arguments
await db.runAsync('UPDATE test SET intValue = ? WHERE value = ?', [999, 'aaa']); // Binding unnamed parameters from array
await db.runAsync('DELETE FROM test WHERE value = $value', { $value: 'aaa' }); // Binding named parameters from object
// `getFirstAsync()` is useful when you want to get a single row from the database.
const firstRow = await db.getFirstAsync('SELECT * FROM test');
console.log(firstRow.id, firstRow.value, firstRow.intValue);
// `getAllAsync()` is useful when you want to get all results as an array of objects.
const allRows = await db.getAllAsync('SELECT * FROM test');
for (const row of allRows) {
 console.log(row.id, row.value, row.intValue);
}
// `getEachAsync()` is useful when you want to iterate SQLite query cursor.
for await (const row of db.getEachAsync('SELECT * FROM test')) {
 console.log(row.id, row.value, row.intValue);
}

Show More

```

### Prepared statements
Prepared statement allows you compile your SQL query once and execute it multiple times with different parameters. You can get a prepared statement by calling [`prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#prepareasyncsource) or [`prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#preparesyncsource) method on a database instance. The prepared statement can fulfill CRUD operations by calling [`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#executeasyncparams) or [`executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#executesyncparams) method.
> Note: Remember to call [`finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#finalizeasync) or [`finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#finalizesync) method to release the prepared statement after you finish using the statement. `try-finally` block is recommended to ensure the prepared statement is finalized.
Prepared statements
Copy
```
const statement = await db.prepareAsync(
 'INSERT INTO test (value, intValue) VALUES ($value, $intValue)'
);
try {
 let result = await statement.executeAsync({ $value: 'bbb', $intValue: 101 });
 console.log('bbb and 101:', result.lastInsertRowId, result.changes);
 result = await statement.executeAsync({ $value: 'ccc', $intValue: 102 });
 console.log('ccc and 102:', result.lastInsertRowId, result.changes);
 result = await statement.executeAsync({ $value: 'ddd', $intValue: 103 });
 console.log('ddd and 103:', result.lastInsertRowId, result.changes);
} finally {
 await statement.finalizeAsync();
}
const statement2 = await db.prepareAsync('SELECT * FROM test WHERE intValue >= $intValue');
try {
 const result = await statement2.executeAsync<{ value: string; intValue: number }>({
  $intValue: 100,
 });
 // `getFirstAsync()` is useful when you want to get a single row from the database.
 const firstRow = await result.getFirstAsync();
 console.log(firstRow.id, firstRow.value, firstRow.intValue);
 // Reset the SQLite query cursor to the beginning for the next `getAllAsync()` call.
 await result.resetAsync();
 // `getAllAsync()` is useful when you want to get all results as an array of objects.
 const allRows = await result.getAllAsync();
 for (const row of allRows) {
  console.log(row.value, row.intValue);
 }
 // Reset the SQLite query cursor to the beginning for the next `for-await-of` loop.
 await result.resetAsync();
 // The result object is also an async iterable. You can use it in `for-await-of` loop to iterate SQLite query cursor.
 for await (const row of result) {
  console.log(row.value, row.intValue);
 }
} finally {
 await statement2.finalizeAsync();
}

Show More

```

### `useSQLiteContext()` hook
useSQLiteContext() hook
Copy
```
import { SQLiteProvider, useSQLiteContext, type SQLiteDatabase } from 'expo-sqlite';
import { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
export default function App() {
 return (
  <View style={styles.container}><SQLiteProvider databaseName="test.db" onInit={migrateDbIfNeeded}><Header /><Content /></SQLiteProvider></View>
 );
}
export function Header() {
 const db = useSQLiteContext();
 const [version, setVersion] = useState('');
 useEffect(() => {
  async function setup() {
   const result = await db.getFirstAsync<{ 'sqlite_version()': string }>(
    'SELECT sqlite_version()'
   );
   setVersion(result['sqlite_version()']);
  }
  setup();
 }, []);
 return (
  <View style={styles.headerContainer}><Text style={styles.headerText}>SQLite version: {version}</Text></View>
 );
}
interface Todo {
 value: string;
 intValue: number;
}
export function Content() {
 const db = useSQLiteContext();
 const [todos, setTodos] = useState<Todo[]>([]);
 useEffect(() => {
  async function setup() {
   const result = await db.getAllAsync<Todo>('SELECT * FROM todos');
   setTodos(result);
  }
  setup();
 }, []);
 return (
  <View style={styles.contentContainer}>{todos.map((todo, index) => (
    <View style={styles.todoItemContainer} key={index}><Text>{`${todo.intValue} - ${todo.value}`}</Text></View>
   ))}</View>
 );
}
async function migrateDbIfNeeded(db: SQLiteDatabase) {
 const DATABASE_VERSION = 1;
 let { user_version: currentDbVersion } = await db.getFirstAsync<{ user_version: number }>(
  'PRAGMA user_version'
 );
 if (currentDbVersion >= DATABASE_VERSION) {
  return;
 }
 if (currentDbVersion === 0) {
  await db.execAsync(`
PRAGMA journal_mode = 'wal';
CREATE TABLE todos (id INTEGER PRIMARY KEY NOT NULL, value TEXT NOT NULL, intValue INTEGER);
`);
  await db.runAsync('INSERT INTO todos (value, intValue) VALUES (?, ?)', 'hello', 1);
  await db.runAsync('INSERT INTO todos (value, intValue) VALUES (?, ?)', 'world', 2);
  currentDbVersion = 1;
 }
 // if (currentDbVersion === 1) {
 //  Add more migrations
 // }
 await db.execAsync(`PRAGMA user_version = ${DATABASE_VERSION}`);
}
const styles = StyleSheet.create({
 // Your styles...
});

Show More

```

### `useSQLiteContext()` hook with `React.Suspense`
As with the [`useSQLiteContext()`](https://docs.expo.dev/versions/latest/sdk/sqlite#usesqlitecontext-hook) hook, you can also integrate the [`SQLiteProvider`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqliteprovider) with [`React.Suspense`](https://react.dev/reference/react/Suspense) to show a fallback component until the database is ready. To enable the integration, pass the `useSuspense` prop to the `SQLiteProvider` component.
useSQLiteContext() hook with React.Suspense
Copy
```
import { SQLiteProvider, useSQLiteContext } from 'expo-sqlite';
import { Suspense } from 'react';
import { View, Text, StyleSheet } from 'react-native';
export default function App() {
 return (
  <View style={styles.container}><Suspense fallback={<Fallback />}><SQLiteProvider databaseName="test.db" onInit={migrateDbIfNeeded} useSuspense><Header /><Content /></SQLiteProvider></Suspense></View>
 );
}

```

### Executing queries within an async transaction
Executing queries within an async transaction
Copy
```
const db = await SQLite.openDatabaseAsync('databaseName');
await db.withTransactionAsync(async () => {
 const result = await db.getFirstAsync('SELECT COUNT(*) FROM USERS');
 console.log('Count:', result.rows[0]['COUNT(*)']);
});

```

Due to the nature of async/await, any query that runs while the transaction is active will be included in the transaction. This includes query statements that are outside of the scope function passed to `withTransactionAsync()` and may be surprising behavior. For example, the following test case runs queries inside and outside of a scope function passed to `withTransactionAsync()`. However, all of the queries will run within the actual SQL transaction because the second `UPDATE` query runs before the transaction finishes.
```
Promise.all([
 // 1. A new transaction begins
 db.withTransactionAsync(async () => {
  // 2. The value "first" is inserted into the test table and we wait 2
  //  seconds
  await db.execAsync('INSERT INTO test (data) VALUES ("first")');
  await sleep(2000);
  // 4. Two seconds in, we read the latest data from the table
  const row = await db.getFirstAsync<{ data: string }>('SELECT data FROM test');
  // ❌ The data in the table will be "second" and this expectation will fail.
  //  Additionally, this expectation will throw an error and roll back the
  //  transaction, including the `UPDATE` query below since it ran within
  //  the transaction.
  expect(row.data).toBe('first');
 }),
 // 3. One second in, the data in the test table is updated to be "second".
 //  This `UPDATE` query runs in the transaction even though its code is
 //  outside of it because the transaction happens to be active at the time
 //  this query runs.
 sleep(1000).then(async () => db.execAsync('UPDATE test SET data = "second"')),
]);

Show More

```

The [`withExclusiveTransactionAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#withexclusivetransactionasynctask) function addresses this. Only queries that run within the scope function passed to `withExclusiveTransactionAsync()` will run within the actual SQL transaction.
### Executing PRAGMA queries
Executing PRAGMA queries
Copy
```
const db = await SQLite.openDatabaseAsync('databaseName');
await db.execAsync('PRAGMA journal_mode = WAL');
await db.execAsync('PRAGMA foreign_keys = ON');

```

> Tip: Enable [WAL journal mode](https://www.sqlite.org/wal.html) when you create a new database to improve performance in general.
### Import an existing database
To open a new SQLite database using an existing .db file you already have, you can use the [`SQLiteProvider`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqliteprovider) with [`assetSource`](https://docs.expo.dev/versions/latest/sdk/sqlite#assetsource).
useSQLiteContext() with existing database
Copy
```
import { SQLiteProvider, useSQLiteContext } from 'expo-sqlite';
import { View, Text, StyleSheet } from 'react-native';
export default function App() {
 return (
  <View style={styles.container}><SQLiteProvider databaseName="test.db" assetSource={{ assetId: require('./assets/test.db') }}><Header /><Content /></SQLiteProvider></View>
 );
}

```

### Sharing a database between apps/extensions (iOS)
To share a database with other apps/extensions in the same App Group, you can use shared containers by following the steps below:
1
Configure the App Group in app config:
app.json
Copy
```
{
 "expo": {
  "ios": {
   "bundleIdentifier": "com.myapp",
   "entitlements": {
    "com.apple.security.application-groups": ["group.com.myapp"]
   }
  }
 }
}

```

2
Use [`Paths.appleSharedContainers`](https://docs.expo.dev/versions/latest/sdk/filesystem-next#applesharedcontainers) from the [`expo-file-system`](https://docs.expo.dev/versions/latest/sdk/filesystem-next) library to retrieve the path to the shared container:
Using Shared Container for SQLite Database on iOS
Copy
```
import { SQLiteProvider, defaultDatabaseDirectory } from 'expo-sqlite';
import { Paths } from 'expo-file-system/next';
import { useMemo } from 'react';
import { Platform, View } from 'react-native';
export default function App() {
 const dbDirectory = useMemo(() => {
  if (Platform.OS === 'ios') {
   return Object.values(Paths.appleSharedContainers)?.[0]?.uri;
   // or `Paths.appleSharedContainers['group.com.myapp']?.uri` to choose specific container
  }
  return defaultDatabaseDirectory;
 }, []);
 return (
  <View style={styles.container}><SQLiteProvider databaseName="test.db" directory={dbDirectory}><Header /><Content /></SQLiteProvider></View>
 );
}

Show More

```

### Passing binary data
Use [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) to pass binary data to the database:
Passing binary data
Copy
```
await db.execAsync(`
DROP TABLE IF EXISTS blobs;
CREATE TABLE IF NOT EXISTS blobs (id INTEGER PRIMARY KEY NOT NULL, data BLOB);
`);
const blob = new Uint8Array([0x00, 0x01, 0x02, 0x03, 0x04, 0x05]);
await db.runAsync('INSERT INTO blobs (data) VALUES (?)', blob);
const row = await db.getFirstAsync<{ data: Uint8Array }>('SELECT * FROM blobs');
expect(row.data).toEqual(blob);

```

### Browse an on-device database
You can inspect a database, execute queries against it, and explore data with the [`drizzle-studio-expo` dev tools plugin](https://github.com/drizzle-team/drizzle-studio-expo). This plugin enables you to launch [Drizzle Studio](https://orm.drizzle.team/drizzle-studio/overview), connected to a database in your app, directly from Expo CLI. This plugin can be used with any `expo-sqlite` configuration. It does not require that you use [Drizzle ORM](https://docs.expo.dev/versions/latest/sdk/sqlite#drizzle-orm) in your app. [Learn how to install and use the plugin](https://github.com/drizzle-team/drizzle-studio-expo).
### Key-value storage
The `expo-sqlite` library provides [`Storage`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitestorage) as a drop-in replacement for the [`@react-native-async-storage/async-storage`](https://github.com/react-native-async-storage/async-storage) library. This key-value store is backed by SQLite. If your project already uses `expo-sqlite`, you can leverage `expo-sqlite/kv-store` without needing to add another dependency.
[`Storage`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitestorage) provides the same API as `@react-native-async-storage/async-storage`:
Using the Store
Copy
```
// The storage API is the default export, you can call it Storage, AsyncStorage, or whatever you prefer.
import Storage from 'expo-sqlite/kv-store';
await Storage.setItem('key', JSON.stringify({ entity: 'value' }));
const value = await Storage.getItem('key');
const entity = JSON.parse(value);
console.log(entity); // { entity: 'value' }

```

A key benefit of using `expo-sqlite/kv-store` is the addition of synchronous APIs for added convenience:
Using the Store with synchronous APIs
Copy
```
// The storage API is the default export, you can call it Storage, AsyncStorage, or whatever you prefer.
import Storage from 'expo-sqlite/kv-store';
Storage.setItemSync('key', 'value');
const value = Storage.getItemSync('key');

```

If you're currently using `@react-native-async-storage/async-storage` in your project, switching to `expo-sqlite/kv-store` is as simple as changing the import statement:
```
- import AsyncStorage from '@react-native-async-storage/async-storage';
+ import AsyncStorage from 'expo-sqlite/kv-store';

```

## Third-party library integrations
The `expo-sqlite` library is designed to be a solid SQLite foundation. It enables broader integrations with third-party libraries for more advanced higher-level features. Here are some of the libraries that you can use with `expo-sqlite`.
### Drizzle ORM
[Drizzle](https://orm.drizzle.team/) is a ["headless TypeScript ORM with a head"](https://orm.drizzle.team/docs/overview). It runs on Node.js, Bun, Deno, and React Native. It also has a CLI companion called [`drizzle-kit`](https://orm.drizzle.team/kit-docs/overview) for generating SQL migrations.
Check out the [Drizzle ORM documentation](https://orm.drizzle.team/) and the [`expo-sqlite` integration guide](https://orm.drizzle.team/docs/get-started/expo-new) for more details.
### Knex.js
[Knex.js](https://knexjs.org/) is a SQL query builder that is ["flexible, portable, and fun to use!"](https://github.com/knex/knex)
Check out the [`expo-sqlite` integration guide](https://github.com/expo/knex-expo-sqlite-dialect) for more details.
## API
### Cheatsheet for the common API
The following table summarizes the common API for [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitedatabase) and [`SQLiteStatement`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitestatement) classes:
[`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitedatabase) methods| [`SQLiteStatement`](https://docs.expo.dev/versions/latest/sdk/sqlite#sqlitestatement) methods| Description| Use Case  
---|---|---|---  
Executes a SQL query, returning information on the changes made.| Ideal for SQL write operations such as `INSERT`, `UPDATE`, `DELETE`.  
[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#executeasyncparams) + [`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#getfirstasync)| Retrieves the first row from the query result.| Suitable for fetching a single row from the database. For example: `getFirstAsync('SELECT * FROM Users WHERE id = ?', userId)`.  
[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#executeasyncparams) + [`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#getallasync)| Fetches all query results at once.| Best suited for scenarios with smaller result sets, such as queries with a LIMIT clause, like `SELECT * FROM Table LIMIT 100`, where you intend to retrieve all results in a single batch.  
[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite#executeasyncparams) + `for-await-of` async iterator| Provides an iterator for result set traversal. This method fetches one row at a time from the database, potentially reducing memory usage compared to `getAllAsync()`.| Recommended for handling large result sets incrementally, such as with infinite scrolling implementations.  
## Component
### `SQLiteProvider`
Android
iOS
macOS
Type: `React.Element[](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<SQLiteProviderProps[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderprops)>`
Context.Provider component that provides a SQLite database to all children. All descendants of this component will be able to access the database using the [`useSQLiteContext`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext) hook.
SQLiteProviderProps
### `assetSource`
Android
iOS
macOS
Optional • Type: `SQLiteProviderAssetSource[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderassetsource)`
Import a bundled database file from the specified asset module.
Example
```
assetSource={{ assetId: require('./assets/db.db') }}

```

### `children`
Android
iOS
macOS
Type: 
The children to render.
### `databaseName`
Android
iOS
macOS
Type: `string`
The name of the database file to open.
### `directory`
Android
iOS
macOS
Optional • Type: `string` • Default: `defaultDatabaseDirectory`
The directory where the database file is located.
### `onError`
Android
iOS
macOS
Optional • Type: `(error: Error[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)) => void` • Default: `rethrow the error`
Handle errors from SQLiteProvider.
### `onInit`
Android
iOS
macOS
Optional • Type: `(db: SQLiteDatabase[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)) => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
A custom initialization handler to run before rendering the children. You can use this to run database migrations or other setup tasks.
### `options`
Android
iOS
macOS
Optional • Type: `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`
Open options.
### `useSuspense`
Android
iOS
macOS
Optional • Type: `boolean` • Default: `false`
Enable [`React.Suspense`](https://react.dev/reference/react/Suspense) integration.
Example
```
export default function App() {
 return (
  <Suspense fallback={<Text>Loading...</Text>}><SQLiteProvider databaseName="test.db" useSuspense={true}><Main /></SQLiteProvider></Suspense>
 );
}

```

## Constants
### `SQLite.AsyncStorage`
Android
iOS
macOS
Type: `SQLiteStorage[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestorage)`
This default instance of the [`SQLiteStorage`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestorage-1) class is used as a drop-in replacement for the `AsyncStorage` module from [`@react-native-async-storage/async-storage`](https://github.com/react-native-async-storage/async-storage).
### `SQLite.defaultDatabaseDirectory`
Android
iOS
macOS
Type: `any`
The default directory for SQLite databases.
### `SQLite.Storage`
Android
iOS
macOS
Type: `SQLiteStorage[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestorage)`
Alias for [`AsyncStorage`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteasyncstorage), given the storage not only offers asynchronous methods.
## Hooks
### `useSQLiteContext()`
Android
iOS
macOS
A global hook for accessing the SQLite database across components. This hook should only be used within a [`<SQLiteProvider>`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteprovider) component.
Returns:
`SQLiteDatabase[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`
Example
```
export default function App() {
 return (
  <SQLiteProvider databaseName="test.db"><Main /></SQLiteProvider>
 );
}
export function Main() {
 const db = useSQLiteContext();
 console.log('sqlite version', db.getFirstSync('SELECT sqlite_version()'));
 return <View />
}

```

## Classes
### `SQLiteDatabase`
Android
iOS
macOS
A SQLite database.
SQLiteDatabase Properties
### `databasePath`
Android
iOS
macOS
Read Only • Type: `string`
### `options`
Android
iOS
macOS
Read Only • Type: `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`
SQLiteDatabase Methods
### `closeAsync()`
Android
iOS
macOS
Close the database.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `closeSync()`
Android
iOS
macOS
Close the database.
Returns:
`void`
### `execAsync(source)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing all the SQL queries.  
Execute all SQL queries in the supplied string.
> Note: The queries are not escaped for you! Be careful when constructing your queries.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `execSync(source)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing all the SQL queries.  
Execute all SQL queries in the supplied string.
> Note: The queries are not escaped for you! Be careful when constructing your queries.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`void`
### `getAllAsync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult.getAllAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasync), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<T[]>`
Example
```
// For unnamed parameters, you pass values in an array.
db.getAllAsync('SELECT * FROM test WHERE intValue = ? AND name = ?', [1, 'Hello']);
// For unnamed parameters, you pass values in variadic arguments.
db.getAllAsync('SELECT * FROM test WHERE intValue = ? AND name = ?', 1, 'Hello');
// For named parameters, you should pass values in object.
db.getAllAsync('SELECT * FROM test WHERE intValue = $intValue AND name = $name', { $intValue: 1, $name: 'Hello' });

```

### `getAllSync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult.getAllSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallsync), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`T[]`
### `getEachAsync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult) `AsyncIterator`, and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).
Returns:
`AsyncIterableIterator[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)<T, any, any>`
Rather than returning Promise, this function returns an [`AsyncIterableIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator). You can use `for await...of` to iterate over the rows from the SQLite query result.
### `getEachSync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult) `Iterator`, and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`IterableIterator[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)<T, any, any>`
This function returns an [`IterableIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator). You can use `for...of` to iterate over the rows from the SQLite query result.
### `getFirstAsync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult.getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasync), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | T>`
### `getFirstSync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult.getFirstSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstsync), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`null | T`
### `isInTransactionAsync()`
Android
iOS
macOS
Asynchronous call to return whether the database is currently in a transaction.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
### `isInTransactionSync()`
Android
iOS
macOS
Synchronous call to return whether the database is currently in a transaction.
Returns:
`boolean`
### `prepareAsync(source)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
Create a [prepared SQLite statement](https://www.sqlite.org/c3ref/prepare.html).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `prepareSync(source)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
Create a [prepared SQLite statement](https://www.sqlite.org/c3ref/prepare.html).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`SQLiteStatement[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement)`
### `runAsync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `runSync(source, params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
source| `string`| A string containing the SQL query.  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`SQLiteRunResult[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliterunresult)`
### `serializeAsync(databaseName)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName(optional)| `string`| The name of the current attached databases. The default value is `main` which is the default database name.Default:`'main'`  
[Serialize the database](https://sqlite.org/c3ref/serialize.html) as `Uint8Array`.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `serializeSync(databaseName)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName(optional)| `string`| The name of the current attached databases. The default value is `main` which is the default database name.Default:`'main'`  
[Serialize the database](https://sqlite.org/c3ref/serialize.html) as `Uint8Array`.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
### `withExclusiveTransactionAsync(task)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
task| `(txn: Transaction[](https://docs.expo.dev/versions/latest/sdk/sqlite/#transaction)) => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`| An async function to execute within a transaction. Any queries inside the transaction must be executed on the `txn` object. The `txn` object has the same interfaces as the [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) object. You can use `txn` like a [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) object.  
Execute a transaction and automatically commit/rollback based on the `task` result.
The transaction may be exclusive. As long as the transaction is converted into a write transaction, the other async write queries will abort with `database is locked` error.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
db.withExclusiveTransactionAsync(async (txn) => {
 await txn.execAsync('UPDATE test SET name = "aaa"');
});

```

### `withTransactionAsync(task)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
task| `() => Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`| An async function to execute within a transaction.  
Execute a transaction and automatically commit/rollback based on the `task` result.
> Note: This transaction is not exclusive and can be interrupted by other async queries.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
Example
```
db.withTransactionAsync(async () => {
 await db.execAsync('UPDATE test SET name = "aaa"');
 //
 // We cannot control the order of async/await order, so order of execution is not guaranteed.
 // The following UPDATE query out of transaction may be executed here and break the expectation.
 //
 const result = await db.getFirstAsync<{ name: string }>('SELECT name FROM Users');
 expect(result?.name).toBe('aaa');
});
db.execAsync('UPDATE test SET name = "bbb"');

```

If you worry about the order of execution, use `withExclusiveTransactionAsync` instead.
### `withTransactionSync(task)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
task| `() => void`| An async function to execute within a transaction.  
Execute a transaction and automatically commit/rollback based on the `task` result.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`void`
### `SQLiteStatement`
Android
iOS
macOS
A prepared statement returned by [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource) or [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource) that can be binded with parameters and executed.
SQLiteStatement Methods
### `executeAsync(params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
Run the prepared statement and return the [`SQLiteExecuteAsyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult) instance.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<SQLiteExecuteAsyncResult[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult)<T>>`
### `executeSync(params)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
params| `SQLiteBindParams[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`| The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.  
Run the prepared statement and return the [`SQLiteExecuteSyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult) instance.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`SQLiteExecuteSyncResult[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult)<T>`
### `finalizeAsync()`
Android
iOS
macOS
Finalize the prepared statement. This will call the [`sqlite3_finalize()`](https://www.sqlite.org/c3ref/finalize.html) C function under the hood.
Attempting to access a finalized statement will result in an error.
> Note: While expo-sqlite will automatically finalize any orphaned prepared statements upon closing the database, it is considered best practice to manually finalize prepared statements as soon as they are no longer needed. This helps to prevent resource leaks. You can use the `try...finally` statement to ensure that prepared statements are finalized even if an error occurs.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `finalizeSync()`
Android
iOS
macOS
Finalize the prepared statement. This will call the [`sqlite3_finalize()`](https://www.sqlite.org/c3ref/finalize.html) C function under the hood.
Attempting to access a finalized statement will result in an error.
> Note: While expo-sqlite will automatically finalize any orphaned prepared statements upon closing the database, it is considered best practice to manually finalize prepared statements as soon as they are no longer needed. This helps to prevent resource leaks. You can use the `try...finally` statement to ensure that prepared statements are finalized even if an error occurs.
Returns:
`void`
### `getColumnNamesAsync()`
Android
iOS
macOS
Get the column names of the prepared statement.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string[]>`
### `getColumnNamesSync()`
Android
iOS
macOS
Get the column names of the prepared statement.
Returns:
`string[]`
### `SQLiteStorage`
Android
iOS
macOS
Key-value store backed by SQLite. This class accepts a `databaseName` parameter in its constructor, which is the name of the database file to use for the storage.
SQLiteStorage Methods
### `clear()`
Android
iOS
macOS
Alias for [`clearAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#clearasync) method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `clearAsync()`
Android
iOS
macOS
Clears all key-value pairs from the storage asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
### `clearSync()`
Android
iOS
macOS
Clears all key-value pairs from the storage synchronously.
Returns:
`boolean`
### `close()`
Android
iOS
macOS
Alias for [`closeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#closeasync-1) method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `closeAsync()`
Android
iOS
macOS
Closes the database connection asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `closeSync()`
Android
iOS
macOS
Closes the database connection synchronously.
Returns:
`void`
### `getAllKeys()`
Android
iOS
macOS
Alias for [`getAllKeysAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallkeysasync) method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string[]>`
### `getAllKeysAsync()`
Android
iOS
macOS
Retrieves all keys stored in the storage asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string[]>`
### `getAllKeysSync()`
Android
iOS
macOS
Retrieves all keys stored in the storage synchronously.
Returns:
`string[]`
### `getItem(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Alias for [`getItemAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getitemasynckey) method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | string>`
### `getItemAsync(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Retrieves the value associated with the given key asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | string>`
### `getItemSync(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Retrieves the value associated with the given key synchronously.
Returns:
`null | string`
### `mergeItem(key, value)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
value| `string`  
Merges the given value with the existing value for the given key asynchronously. If the existing value is a JSON object, performs a deep merge.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `multiGet(keys)`
Android
iOS
macOS
Parameter| Type  
---|---  
keys| `string[]`  
Retrieves the values associated with the given keys asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<undefined>`
### `multiMerge(keyValuePairs)`
Android
iOS
macOS
Parameter| Type  
---|---  
keyValuePairs| `undefined`  
Merges multiple key-value pairs asynchronously. If existing values are JSON objects, performs a deep merge.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `multiRemove(keys)`
Android
iOS
macOS
Parameter| Type  
---|---  
keys| `string[]`  
Removes the values associated with the given keys asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `multiSet(keyValuePairs)`
Android
iOS
macOS
Parameter| Type  
---|---  
keyValuePairs| `undefined`  
Sets multiple key-value pairs asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `removeItem(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Alias for [`removeItemAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#removeitemasynckey) method.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `removeItemAsync(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Removes the value associated with the given key asynchronously.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`
### `removeItemSync(key)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
Removes the value associated with the given key synchronously.
Returns:
`boolean`
### `setItem(key, value)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
value| `string | SQLiteStorageSetItemUpdateFunction[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestoragesetitemupdatefunction)`  
Alias for [`setItemAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#setitemasynckey-value).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `setItemAsync(key, value)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
value| `string | SQLiteStorageSetItemUpdateFunction[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestoragesetitemupdatefunction)`  
Sets the value for the given key asynchronously. If a function is provided, it computes the new value based on the previous value.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `setItemSync(key, value)`
Android
iOS
macOS
Parameter| Type  
---|---  
key| `string`  
value| `string | SQLiteStorageSetItemUpdateFunction[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestoragesetitemupdatefunction)`  
Sets the value for the given key synchronously. If a function is provided, it computes the new value based on the previous value.
Returns:
`void`
## Methods
### `SQLite.deleteDatabaseAsync(databaseName, directory)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName| `string`| The name of the database file to delete.  
directory(optional)| `string`| The directory where the database file is located. The default value is `defaultDatabaseDirectory`.  
Delete a database file.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `SQLite.deleteDatabaseSync(databaseName, directory)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName| `string`| The name of the database file to delete.  
directory(optional)| `string`| The directory where the database file is located. The default value is `defaultDatabaseDirectory`.  
Delete a database file.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`void`
### `SQLite.deserializeDatabaseAsync(serializedData, options)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
serializedData| | The binary array to deserialize from [`SQLiteDatabase.serializeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializeasyncdatabasename).  
options(optional)| `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`| Open options.  
Given a `Uint8Array` data and [deserialize to memory database](https://sqlite.org/c3ref/deserialize.html).
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `SQLite.deserializeDatabaseSync(serializedData, options)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
serializedData| | The binary array to deserialize from [`SQLiteDatabase.serializeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializesyncdatabasename)  
options(optional)| `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`| Open options.  
Given a `Uint8Array` data and [deserialize to memory database](https://sqlite.org/c3ref/deserialize.html).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`SQLiteDatabase[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`
### `SQLite.openDatabaseAsync(databaseName, options, directory)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName| `string`| The name of the database file to open.  
options(optional)| `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`| Open options.  
directory(optional)| `string`| The directory where the database file is located. The default value is `defaultDatabaseDirectory`.  
Open a database.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
### `SQLite.openDatabaseSync(databaseName, options, directory)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
databaseName| `string`| The name of the database file to open.  
options(optional)| `SQLiteOpenOptions[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`| Open options.  
directory(optional)| `string`| The directory where the database file is located. The default value is `defaultDatabaseDirectory`.  
Open a database.
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Returns:
`SQLiteDatabase[](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`
## Event Subscriptions
### `SQLite.addDatabaseChangeListener(listener)`
Android
iOS
macOS
Parameter| Type| Description  
---|---|---  
listener| `(event: DatabaseChangeEvent[](https://docs.expo.dev/versions/latest/sdk/sqlite/#databasechangeevent)) => void`| A function that receives the `databaseName`, `databaseFilePath`, `tableName` and `rowId` of the modified data.  
Add a listener for database changes.
> Note: to enable this feature, you must set [`enableChangeListener` to `true`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions) when opening the database.
Returns:
`EventSubscription`
A `Subscription` object that you can call `remove()` on when you would like to unsubscribe the listener.
## Interfaces
### `SQLiteExecuteAsyncResult`
Android
iOS
macOS
Extends: `AsyncIterableIterator[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)<T>`
A result returned by [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams).
Example
The result includes the [`lastInsertRowId`](https://www.sqlite.org/c3ref/last_insert_rowid.html) and [`changes`](https://www.sqlite.org/c3ref/changes.html) properties. You can get the information from the write operations.
```
const statement = await db.prepareAsync('INSERT INTO test (value) VALUES (?)');
try {
 const result = await statement.executeAsync(101);
 console.log('lastInsertRowId:', result.lastInsertRowId);
 console.log('changes:', result.changes);
} finally {
 await statement.finalizeAsync();
}

```

Example
The result implements the [`AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator) interface, so you can use it in `for await...of` loops.
```
const statement = await db.prepareAsync('SELECT value FROM test WHERE value > ?');
try {
 const result = await statement.executeAsync<{ value: number }>(100);
 for await (const row of result) {
  console.log('row value:', row.value);
 }
} finally {
 await statement.finalizeAsync();
}

```

Example
If your write operations also return values, you can mix all of them together.
```
const statement = await db.prepareAsync('INSERT INTO test (name, value) VALUES (?, ?) RETURNING name');
try {
 const result = await statement.executeAsync<{ name: string }>('John Doe', 101);
 console.log('lastInsertRowId:', result.lastInsertRowId);
 console.log('changes:', result.changes);
 for await (const row of result) {
  console.log('name:', row.name);
 }
} finally {
 await statement.finalizeAsync();
}

```

Property| Type| Description  
---|---|---  
changes| `number`| The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.  
lastInsertRowId| `number`| The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.  
SQLiteExecuteAsyncResult Methods
### `getAllAsync()`
Android
iOS
macOS
Get all rows of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetasync). Otherwise, an error will be thrown.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<T[]>`
### `getFirstAsync()`
Android
iOS
macOS
Get the first row of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetasync). Otherwise, an error will be thrown.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | T>`
### `resetAsync()`
Android
iOS
macOS
Reset the prepared statement cursor. This will call the [`sqlite3_reset()`](https://www.sqlite.org/c3ref/reset.html) C function under the hood.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`
### `SQLiteExecuteSyncResult`
Android
iOS
macOS
Extends: 
A result returned by [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams).
> Note: Running heavy tasks with this function can block the JavaScript thread and affect performance.
Example
The result includes the [`lastInsertRowId`](https://www.sqlite.org/c3ref/last_insert_rowid.html) and [`changes`](https://www.sqlite.org/c3ref/changes.html) properties. You can get the information from the write operations.
```
const statement = db.prepareSync('INSERT INTO test (value) VALUES (?)');
try {
 const result = statement.executeSync(101);
 console.log('lastInsertRowId:', result.lastInsertRowId);
 console.log('changes:', result.changes);
} finally {
 statement.finalizeSync();
}

```

Example
The result implements the [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) interface, so you can use it in `for...of` loops.
```
const statement = db.prepareSync('SELECT value FROM test WHERE value > ?');
try {
 const result = statement.executeSync<{ value: number }>(100);
 for (const row of result) {
  console.log('row value:', row.value);
 }
} finally {
 statement.finalizeSync();
}

```

Example
If your write operations also return values, you can mix all of them together.
```
const statement = db.prepareSync('INSERT INTO test (name, value) VALUES (?, ?) RETURNING name');
try {
 const result = statement.executeSync<{ name: string }>('John Doe', 101);
 console.log('lastInsertRowId:', result.lastInsertRowId);
 console.log('changes:', result.changes);
 for (const row of result) {
  console.log('name:', row.name);
 }
} finally {
 statement.finalizeSync();
}

```

Property| Type| Description  
---|---|---  
changes| `number`| The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.  
lastInsertRowId| `number`| The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.  
SQLiteExecuteSyncResult Methods
### `getAllSync()`
Android
iOS
macOS
Get all rows of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetsync). Otherwise, an error will be thrown.
Returns:
`T[]`
### `getFirstSync()`
Android
iOS
macOS
Get the first row of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetsync). Otherwise, an error will be thrown.
Returns:
`null | T`
### `resetSync()`
Android
iOS
macOS
Reset the prepared statement cursor. This will call the [`sqlite3_reset()`](https://www.sqlite.org/c3ref/reset.html) C function under the hood.
Returns:
`void`
### `SQLiteOpenOptions`
Android
iOS
macOS
Options for opening a database.
Property| Type| Description  
---|---|---  
enableChangeListener(optional)| `boolean`| Whether to call the [`sqlite3_update_hook()`](https://www.sqlite.org/c3ref/update_hook.html) function and enable the `onDatabaseChange` events. You can later subscribe to the change events by [`addDatabaseChangeListener`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteadddatabasechangelistenerlistener).Default:`false`  
enableCRSQLite(optional)| `boolean`| 
> Deprecated CR-SQLite is no longer actively maintained. Its support is deprecated in SDK 52, and the option will be removed in SDK 53.
Whether to enable the CR-SQLite extension.Default:`false`  
useNewConnection(optional)| `boolean`| Whether to create new connection even if connection with the same database name exists in cache.Default:`false`  
### `SQLiteProviderAssetSource`
Android
iOS
macOS
Property| Type| Description  
---|---|---  
assetId| `number`| The asset ID returned from the `require()` call.  
forceOverwrite(optional)| `boolean`| Force overwrite the local database file even if it already exists.Default:`false`  
### `SQLiteRunResult`
Android
iOS
macOS
A result returned by [`SQLiteDatabase.runAsync`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runasyncsource-params) or [`SQLiteDatabase.runSync`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runsyncsource-params).
Property| Type| Description  
---|---|---  
changes| `number`| The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.  
lastInsertRowId| `number`| The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.  
## Types
### `DatabaseChangeEvent`
Android
iOS
macOS
The event payload for the listener of [`addDatabaseChangeListener`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteadddatabasechangelistenerlistener)
Property| Type| Description  
---|---|---  
databaseFilePath| `string`| The absolute file path to the database.  
databaseName| `string`| The database name. The value would be `main` by default and other database names if you use `ATTACH DATABASE` statement.  
rowId| `number`| The changed row ID.  
tableName| `string`| The table name.  
### `SQLiteBindParams`
Android
iOS
macOS
Literal Type: `Record`
Acceptable values are: `Record<string, >`
### `SQLiteBindValue`
Android
iOS
macOS
Literal Type: `union`
Bind parameters to the prepared statement. You can either pass the parameters in the following forms:
Example
A single array for unnamed parameters.
```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = ? AND intValue = ?');
const result = await statement.executeAsync(['test1', 789]);
const firstRow = await result.getFirstAsync();

```

Example
Variadic arguments for unnamed parameters.
```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = ? AND intValue = ?');
const result = await statement.executeAsync('test1', 789);
const firstRow = await result.getFirstAsync();

```

Example
A single object for [named parameters](https://www.sqlite.org/lang_expr.html)
We support multiple named parameter forms such as `:VVV`, `@VVV`, and `$VVV`. We recommend using `$VVV` because JavaScript allows using `$` in identifiers without escaping.
```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = $value AND intValue = $intValue');
const result = await statement.executeAsync({ $value: 'test1', $intValue: 789 });
const firstRow = await result.getFirstAsync();

```

Acceptable values are: `string` | `number` | `null` | `boolean` | 
### `SQLiteStorageSetItemUpdateFunction(prevValue)`
Android
iOS
macOS
Update function for the [`setItemAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#setitemasynckey-value) or [`setItemSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#setitemsynckey-value) method. It computes the new value based on the previous value. The function returns the new value to set for the key.
Parameter| Type| Description  
---|---|---  
prevValue| `string | null`| The previous value associated with the key, or `null` if the key was not set.  
Returns:
`string`
### `SQLiteVariadicBindParams`
Android
iOS
macOS
Type: `SQLiteBindValue[][](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue)`

