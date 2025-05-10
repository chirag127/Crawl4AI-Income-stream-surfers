---
url: https://docs.expo.dev/versions/latest/sdk/filesystem-next
title: https://docs.expo.dev/versions/latest/sdk/filesystem-next
date: 2025-04-30T17:16:17.706916
depth: 2
---

Search
`Ctrl` `K`
[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)
Reference version
SDK 52 (latest)
[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo FileSystem (next)
A library that provides access to the local file system on the device.
Android
iOS
tvOS
Bundled version:
~18.0.12
> The `next` version of the FileSystem API is included in the `expo-file-system` library. It can be used alongside the previous API, and offers a simplified, object oriented way of performing filesystem operations.
> To provide quicker updates, `expo-file-system/next` is currently unsupported in Expo Go and Snack. To use it, create a [development build](https://docs.expo.dev/develop/development-builds/create-a-build).
`expo-file-system/next` provides access to the file system stored locally on the device. It can also download files from the network.
## Installation
Terminal
Copy
`- ``npx expo install expo-file-system`
If you are installing this in an [existing React Native app](https://docs.expo.dev/bare/overview), make sure to [install `expo`](https://docs.expo.dev/bare/installing-expo-modules) in your project.
## Usage
### Writing and reading text files
example.ts
Copy
```
import { File, Paths } from 'expo-file-system/next';
try {
 const file = new File(Paths.cache, 'example.txt');
 file.create(); // can throw an error if the file already exists or no permission to create it
 file.write('Hello, world!');
 console.log(file.text()); // Hello, world!
} catch (error) {
 console.error(error);
}

```

### Downloading files
example.ts
Copy
```
import { File, Paths } from 'expo-file-system/next';
const url = 'https://pdfobject.com/pdf/sample.pdf';
const destination = new Directory(Paths.cache, 'pdfs');
try {
 destination.create();
 const output = await File.downloadFileAsync(url, destination);
 console.log(output.exists); // true
 console.log(output.uri); // path to the downloaded file, e.g. '${cacheDirectory}/pdfs/sample.pdf'
} catch (error) {
 console.error(error);
}

```

### Moving and copying files
example.ts
Copy
```
import { File, Paths } from 'expo-file-system/next';
try {
 const file = new File(Paths.document, 'example.txt');
 file.create();
 console.log(file.uri); // '${documentDirectory}/example.txt'
 file.move(Paths.cache);
 console.log(file.uri); // '${cacheDirectory}/example.txt'
 file.move(new Directory(Paths.cache, 'newFolder'));
 console.log(file.uri); // '${cacheDirectory}/newFolder/example.txt'
} catch (error) {
 console.error(error);
}

```

### Using legacy FileSystem API
example.ts
Copy
```
import * as FileSystem from 'expo-file-system';
import { File, Paths } from 'expo-file-system/next';
try {
 const file = new File(Paths.cache, 'example.txt');
 const content = await FileSystem.readAsStringAsync(file.uri);
 console.log(content);
} catch (error) {
 console.error(error);
}

```

### Listing directory contents recursively
example.ts
Copy
```
import { Directory, Paths } from 'expo-file-system/next';
function printDirectory(directory: Directory, indent: number = 0) {
 console.log(`${' '.repeat(indent)} + ${directory.name}`);
 const contents = directory.list();
 for (const item of contents) {
  if (item instanceof Directory) {
   printDirectory(item, indent + 2);
  } else {
   console.log(`${' '.repeat(indent + 2)} - ${item.name} (${item.size} bytes)`);
  }
 }
}
try {
 printDirectory(new Directory(Paths.cache));
} catch (error) {
 console.error(error);
}

Show More

```

## API
## Classes
### `Directory`
Android
iOS
tvOS
Type: Class extends `FileSystemDirectory`
Represents a directory on the filesystem.
A `Directory` instance can be created for any path, and does not need to exist on the filesystem during creation.
Directory Properties
### `exists`
Android
iOS
tvOS
Type: `boolean`
A boolean representing if a directory exists. `true` if the directory exists, `false` otherwise. Also `false` if the application does not have read access to the file.
### `uri`
Android
iOS
tvOS
Read Only • Type: `string`
Represents the directory URI. The field is read-only, but it may change as a result of calling some methods such as `move`.
### `name`
Android
iOS
tvOS
Type: `string`
Directory name.
### `parentDirectory`
Android
iOS
tvOS
Type: 
Directory containing the file.
Directory Methods
### `copy(destination)`
Android
iOS
tvOS
Parameter| Type  
---|---  
destination| ``  
Copies a directory.
Returns:
`any`
### `create()`
Android
iOS
tvOS
Creates a directory that the current uri points to.
Returns:
`void`
### `delete()`
Android
iOS
tvOS
Deletes a directory. Also deletes all files and directories inside the directory.
Returns:
`void`
### `list()`
Android
iOS
tvOS
Lists the contents of a directory. Calling this method if the parent directory does not exist will throw an error.
Returns:
`()[]`
An array of `Directory` and `File` instances.
### `move(destination)`
Android
iOS
tvOS
Parameter| Type  
---|---  
destination| ``  
Moves a directory. Updates the `uri` property that now points to the new location.
Returns:
`any`
### `File`
Android
iOS
tvOS
Type: Class extends `FileSystemFile`
File Properties
### `exists`
Android
iOS
tvOS
Type: `boolean`
A boolean representing if a file exists. `true` if the file exists, `false` otherwise. Also `false` if the application does not have read access to the file.
### `md5`
Android
iOS
tvOS
Literal type: `union`
An md5 hash of the file. Null if the file does not exist or it cannot be read.
Acceptable values are: `null` | `string`
### `size`
Android
iOS
tvOS
Literal type: `union`
A size of the file in bytes. Null if the file does not exist or it cannot be read.
Acceptable values are: `null` | `number`
### `uri`
Android
iOS
tvOS
Read Only • Type: `string`
Represents the file URI. The field is read-only, but it may change as a result of calling some methods such as `move`.
### `extension`
Android
iOS
tvOS
Type: `string`
File extension.
Example
`'.png'`
### `name`
Android
iOS
tvOS
Type: `string`
File name. Includes the extension.
### `parentDirectory`
Android
iOS
tvOS
Type: 
Directory containing the file.
File Methods
### `base64()`
Android
iOS
tvOS
Retrieves content of the file as base64.
Returns:
`string`
The contents of the file as a base64 string.
### `bytes()`
Android
iOS
tvOS
Retrieves byte content of the entire file.
Returns:
The contents of the file as a Uint8Array.
### `copy(destination)`
Android
iOS
tvOS
Parameter| Type  
---|---  
destination| ``  
Copies a file.
Returns:
`any`
### `create()`
Android
iOS
tvOS
Creates a file.
Returns:
`void`
### `delete()`
Android
iOS
tvOS
Deletes a file.
Returns:
`void`
### `downloadFileAsync(url, destination)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
url| `string`| The URL of the file to download.  
destination| ``| The destination directory or file. If a directory is provided, the resulting filename will be determined based on the response headers.  
A static method that downloads a file from the network.
Returns:
`Promise[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<>`
A promise that resolves to the downloaded file.
Example
```
const file = await File.downloadFileAsync("https://example.com/image.png", new Directory(Paths.document));

```

### `move(destination)`
Android
iOS
tvOS
Parameter| Type  
---|---  
destination| ``  
Moves a directory. Updates the `uri` property that now points to the new location.
Returns:
`any`
### `open()`
Android
iOS
tvOS
Returns a FileHandle object that can be used to read and write data to the file.
Returns:
### `readableStream()`
Android
iOS
tvOS
Returns:
`ReadableStream[](https://docs.expo.dev/versions/latest/sdk/filesystem-next/#readablestream)<>`
### `text()`
Android
iOS
tvOS
Retrieves text from the file.
Returns:
`string`
The contents of the file as string.
### `writableStream()`
Android
iOS
tvOS
Returns:
`WritableStream[](https://docs.expo.dev/versions/latest/sdk/filesystem-next/#writablestream)<>`
### `write(content)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
content| `string | `| The content to write into the file.  
Writes content to the file.
Returns:
`void`
### `Paths`
Android
iOS
tvOS
Type: Class extends `PathUtilities`
Paths Properties
### `appleSharedContainers`
Android
iOS
tvOS
Type: `Record<string, >`
### `cache`
Android
iOS
tvOS
Type: 
A property containing the cache directory – a place to store files that can be deleted by the system when the device runs low on storage.
### `document`
Android
iOS
tvOS
Type: 
A property containing the document directory – a place to store files that are safe from being deleted by the system.
Paths Methods
### `basename(path, ext)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to get the base name from.  
ext(optional)| `string`| An optional file extension.  
Returns the base name of a path.
Returns:
`string`
A string representing the base name.
### `dirname(path)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to get the directory name from.  
Returns the directory name of a path.
Returns:
`string`
A string representing the directory name.
### `extname(path)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to get the extension from.  
Returns the extension of a path.
Returns:
`string`
A string representing the extension.
### `isAbsolute(path)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to check.  
Checks if a path is absolute.
Returns:
`boolean`
`true` if the path is absolute, `false` otherwise.
### `join(...paths)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
...paths| `(string | )[]`| An array of path segments.  
Joins path segments into a single path.
Returns:
`string`
A string representing the joined path.
### `normalize(path)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to normalize.  
Normalizes a path.
Returns:
`string`
A string representing the normalized path.
### `parse(path)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
path| `string | `| The path to parse.  
Parses a path into its components.
Returns:
`{  base: string,   dir: string,   ext: string,   name: string,   root: string }`
An object containing the parsed path components.
### `relative(from, to)`
Android
iOS
tvOS
Parameter| Type| Description  
---|---|---  
from| `string | `| The base path.  
to| `string | `| The relative path.  
Resolves a relative path to an absolute path.
Returns:
`string`
A string representing the resolved path.

