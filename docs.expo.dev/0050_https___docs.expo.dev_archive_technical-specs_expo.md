---
url: https://docs.expo.dev/archive/technical-specs/expo-updates-0
title: https://docs.expo.dev/archive/technical-specs/expo-updates-0
date: 2025-04-30T17:12:45.567830
depth: 2
---

[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)
# Expo Updates v0
Version 0
Updated 2021-12-01
## Introduction
This is the specification for Expo Updates, a protocol for delivering updates to Expo apps running on multiple platforms.
### Conformance
Conforming servers and client libraries must fulfill all normative requirements. Conformance requirements are described in this document by both descriptive assertions and key words with clearly defined meanings.
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the normative portions of this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119). These key words may appear in lowercase and still retain their meaning unless explicitly declared as non-normative.
A conforming implementation of this protocol may provide additional functionality, but must not where explicitly disallowed or would otherwise result in non-conformance.
### Overview
Conforming servers and client libraries MUST follow the HTTP spec as described in [RFC 7231](https://tools.ietf.org/html/rfc7231) as well as the more precise guidance described in this spec.
An _update_ is defined as a [_manifest_](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response) together with the assets referenced inside the manifest. Expo Updates is a protocol for assembling and delivering updates to apps running on multiple platforms.
An app running a conformant Expo Updates client library MUST load the most recent update saved in the client library's cache, possibly after filtering by the contents of the manifest's [_metadata_](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-body).
The following describes how a conformant Expo Updates client library MUST retrieve a new update from a conformant server:
  1. The client library will make a [request](https://docs.expo.dev/archive/technical-specs/expo-updates-0#request) for the most recent manifest, with constraints specified in the headers.
  2. If a new manifest is downloaded, the client library will proceed to make additional requests to download and store any missing assets specified in the manifest.
  3. The client library will edit its local state to reflect that a new update has been added to the local cache. It will also update the local state with the new `expo-manifest-filters` and `expo-server-defined-headers` found in the response [headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-headers).


The primary consumers of this spec are Expo Application Services and organizations that wish to manage their own update server to satisfy internal requirements.
## Manifest request
A conformant client library MUST make a GET request with the headers:
  1. `expo-platform`, to specify the platform type the client is running on. 
     * iOS MUST be `expo-platform: ios`.
     * Android MUST be `expo-platform: android`.
     * If it is not one of these platforms, the server SHOULD return a 400 or a 404
  2. `expo-runtime-version` MUST be a runtime version compatible with the client. A runtime version stipulates the native code setup a client is running. It should be set when the client is built. For example, in an iOS client, the value may be set in a plist file.
  3. Any headers stipulated by a previous responses' [server defined headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-headers).


A conformant client library MUST send at least one of `accept: application/expo+json`, `accept: application/json`, or `accept: multipart/mixed` based on the supported response structures though SHOULD send `accept: application/expo+json, application/json, multipart/mixed`. A conformant client library MAY express preference using "q" parameters as specified in [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#section-5.3.1), which default to `1`.
A conformant client library configured to perform [code signing](https://docs.expo.dev/archive/technical-specs/expo-updates-0#code-signing) verification MUST send a `expo-expect-signature` header to indicate that it expects the conformant server to include the `expo-signature` header in the manifest response. `expo-expect-signature` is an [Expo SFV](https://docs.expo.dev/technical-specs/expo-sfv-0) dictionary which MAY contain any of the following key value pairs:
  * `sig` SHOULD contain the boolean `true` to indicate that it requires a conformant server to respond with the signature in the `sig` key.
  * `keyid` SHOULD contain the keyId of the public key the client will use to verify the signature
  * `alg` SHOULD contain the algorithm the client will use to verify the signature


Example:
```
accept: application/expo+json;q=0.9, application/json;q=0.8, multipart/mixed
expo-platform: *
expo-runtime-version: *
expo-expect-signature: sig, keyid="root", alg="rsa-v1_5-sha256"

```

## Manifest response
A conformant server MUST return a response structured in at least one of two ways. A conformant server MAY support either or both response structures, and when an unsupported response structure is requested the server SHOULD respond with an HTTP `406` error status.
  * For a response with `content-type: application/json` or `content-type: application/expo+json`, the [manifest headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-headers) MUST be sent in the response headers and the [manifest body](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-body) MUST be sent in the response body.
  * For a response with `content-type: multipart/mixed`, the response MUST be structured as specified in the [multipart manifest response](https://docs.expo.dev/archive/technical-specs/expo-updates-0#multipart-manifest-response) section.


The choice of manifest and headers are dependent on the values of the request headers. A conformant server MUST respond with a manifest for the most recent update, ordered by creation time, satisfying all parameters and constraints imposed by the [request headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-request). The server MAY use any properties of the request like its headers and source IP address to choose amongst several updates that all satisfy the request's constraints.
### Manifest response headers
```
expo-protocol-version: 0
expo-sfv-version: 0
expo-manifest-filters: &lt;expo-sfv&gt;
expo-server-defined-headers: &lt;expo-sfv&gt;
cache-control: *
content-type: *
expo-signature: *

```

  * `expo-protocol-version` describes the version of the protocol defined in this spec and MUST be `0`.
  * `expo-sfv-version` MUST be `0`.
  * `expo-manifest-filters` is an [Expo SFV](https://docs.expo.dev/technical-specs/expo-sfv-0) dictionary. It is used to filter updates stored by the client library by the `metadata` attribute found in the [manifest](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-body). If a field is mentioned in the filter, the corresponding field in the metadata must either be missing or equal for the update to be included. The client library MUST store the manifest filters until it is overwritten by a newer response.
  * `expo-server-defined-headers` is an [Expo SFV](https://docs.expo.dev/technical-specs/expo-sfv-0) dictionary. It defines headers that a client library MUST store until overwritten by a newer dictionary, and they MUST be included in every subsequent [manifest request](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-request).
  * `cache-control` MUST be set to an appropriately short period of time. A value of `cache-control: private, max-age=0` is recommended to ensure the newest manifest is returned. Setting longer cache ages could result in stale updates.
  * `content-type` MUST be determined by _proactive negotiation_ as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-3.4.1). Since the client library is [required](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-request) to send an `accept` header with each manifest request, this will always be either `application/expo+json`, `application/json`; otherwise the request would return a `406` error.
  * `expo-signature` SHOULD contain the signature of the manifest to be used during the validation step of [code signing](https://docs.expo.dev/archive/technical-specs/expo-updates-0#code-signing) if the request for the manifest contained the `expo-expect-signature` header. This is an [Expo SFV](https://docs.expo.dev/technical-specs/expo-sfv-0) dictionary which MAY contain any of the following key value pairs: 
    * `sig` MUST contain the signature of the manifest. The name of this field matches that of `expo-expect-signature`.
    * `keyid` MAY contain the keyId of the key the server used to sign the response. The client SHOULD use the certificate that matches this `keyid` to verify the signature.
    * `alg` MAY contain the algorithm the server used to sign the response. The client SHOULD use this field only if it matches the algorithm defined for the certificate matching `keyid`.


### Manifest response body
The body of the response MUST be a manifest, which is defined as JSON conforming to both the following `Manifest` definition expressed in [TypeScript](https://www.typescriptlang.org/) and the detailed descriptions for each field:
```
type Manifest = {
 id: string;
 createdAt: string;
 runtimeVersion: string;
 launchAsset: Asset;
 assets: Asset[];
 metadata: { [key: string]: string };
 extra: { [key: string]: any };
};
type Asset = {
 hash?: string;
 key: string;
 contentType: string;
 fileExtension?: string;
 url: string;
};

```

  * `id`: The ID MUST uniquely specify the manifest.
  * `createdAt`: The date and time at which the update was created is essential as the client library selects the most recent update (subject to any constraints supplied by the `expo-manifest-filters` header). The datetime should be formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).
  * `runtimeVersion`: Can be any string defined by the developer. It stipulates what native code setup is required to run the associated update.
  * `launchAsset`: A special asset that is the entry point of the application code. The `fileExtension` field will be ignored for this asset and SHOULD be omitted.
  * `assets`: An array of assets used by the update bundle, such as JavaScript, pictures, and fonts. All assets (including the `launchAsset`) should be downloaded to disk before executing the update, and a mapping of asset `key`s to locations on disk should be provided to application code.
  * Properties of each asset object: 
    * `hash`: Base64URL-encoded SHA-256 hash of the file to guarantee integrity. Base64URL encoding is defined by [IETF RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-5).
    * `key`: Key used to reference this asset from the update's application code. This key, for example, may be generated by a separate build step that processes the application code, such as a bundler.
    * `contentType`: The MIME type of the file as defined by [RFC 2045](https://tools.ietf.org/html/rfc2045). For example, `application/javascript`, `image/jpeg`.
    * `fileExtension`: The suggested extension to use when a file is saved on a client. Some platforms, such as iOS, require certain file types to be saved with an extension. The extension MUST be prefixed with a `.`. For example, .jpeg. In some cases, such as the launchAsset, this field will be ignored in favor of a locally determined extension. If the field is omitted and there is no locally stipulated extension, the asset will be saved without an extension. For example, `./filename` with no `.` at the end. A conforming client SHOULD prefix a file extension with a `.` if a file extension is not empty and missing the `.` prefix.
    * `url`: Location at which the file may be fetched.
  * `metadata`: The metadata associated with an update. It is a string-valued dictionary. The server MUST send back an empty object at a minimum, but MAY send back anything it wishes within the object to be used for filtering the updates. The metadata MUST pass the filter defined in the accompanying `expo-manifest-filters` header.
  * `extra`: For specification of optional "extra" information such as third-party configuration. The server MUST send back an empty object at a minimum. Expo Updates does not specify or rely upon this field, but other libraries may. For example, if the update is hosted on Expo Application Services (EAS), the EAS project ID and app config (which is used by many Expo libraries through `expo-constants`) may be included:

```
"extra": {
 "eas": {
  "projectId": "00000000-0000-0000-0000-000000000000"
 },
 "expoConfig": {
  "name": "...",
  "version": "...",
  "iconUrl": "...",
  %%placeholder-start%%... %%placeholder-end%%
 },
}

```

### Multipart manifest response
A manifest response of this format is defined by the `multipart/mixed` MIME type as defined by [RFC 2046](https://tools.ietf.org/html/rfc2046#section-5.1).
Headers for this response format are the same as [manifest response headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-headers), with the following exceptions:
  * `content-type` should have a `multipart/mixed` value as defined by [RFC 2046](https://tools.ietf.org/html/rfc2046#section-5.1)
  * `expo-signature` should be included in the `manifest` part headers below if codesigning is being used.


Each part is defined as follows:
  1. REQUIRED `"manifest"` part: 
     * MUST have part header `content-disposition: inline; name="manifest"`.
     * MUST have part header `content-type: application/json` or `application/expo+json`.
     * SHOULD have part header `expo-signature` as defined in [manifest response headers](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-headers) if code signing is being used.
     * The [manifest body](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-response-body) MUST be sent in the part body.
  2. OPTIONAL `"extensions"` part: 
     * MUST have part header `content-disposition: inline; name="extensions"`.
     * MUST have part header `content-type: application/json`.
     * The [manifest extensions](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-extensions) MUST be sent in the part body.


### Manifest extensions
Defined as JSON conforming to both the following `ManifestExtensions` definition expressed in [TypeScript](https://www.typescriptlang.org/) and the detailed descriptions for each field:
```
type ManifestExtensions = {
 assetRequestHeaders: ExpoAssetHeaderDictionary;
 ...
}
type ExpoAssetHeaderDictionary = {
 [assetKey: string]: {
  [headerName: string]: string,
 };
}

```

  * `assetRequestHeaders`: MAY contain a dictionary of header (key, value) pairs to include with asset requests. Key and value MUST both be strings.


## Asset request
A conformant client library MUST make a GET request to the asset URLs specified by the manifest. The client library SHOULD include a header accepting the asset's content type as specified in the manifest. Additionally, the client library SHOULD specify the compression encoding the client library is capable of handling.
Example headers:
```
accept: image/jpeg, */*
accept-encoding: br, gzip

```

A conformant client library MUST also include any header (key, value) pairs included in [`assetRequestHeaders`](https://docs.expo.dev/archive/technical-specs/expo-updates-0#manifest-extensions) for this asset key.
## Asset response
An asset located at a particular URL MUST NOT be changed or removed since client libraries may fetch assets for any update at any time. A conformant client MUST verify that the base64url-encoded SHA-256 hash of the asset matches the `hash` field for the asset from the manifest.
### Asset response headers
The asset MUST be encoded using a compression format that the client supports according to the request's `accept-encoding` header. The server MAY serve uncompressed assets. The response MUST include a `content-type` header with the MIME type of the asset. For example:
```
content-encoding: br
content-type: application/javascript

```

An asset is RECOMMENDED to be served with a `cache-control` header set to a long duration as an asset located at a given URL must not change. For example:
```
cache-control: public, max-age=31536000, immutable

```

### Compression
Assets SHOULD be capable of being served with [Gzip](https://www.gnu.org/software/gzip/) and [Brotli](https://github.com/google/brotli) compression.
## Code signing
Expo Updates supports code signing the manifest. This also transitively signs the assets since their hashes are present in the manifest and verified by a conformant client. A conformant client MAY request the manifest be signed using a private key, and then MUST verify the signature of the manifest using the corresponding code signing certificate before it is used or any corresponding assets are downloaded. The client MUST verify that the signing certificate is either a self-signed, trusted root certificate or is in a certificate chain signed by a trusted root certificate. In either case, the root certificate MUST be embedded in the application or device's operating system.
## Client library
See the [reference client library](https://github.com/expo/expo/tree/main/packages/expo-updates).

