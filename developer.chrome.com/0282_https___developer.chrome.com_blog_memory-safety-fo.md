---
url: https://developer.chrome.com/blog/memory-safety-fonts?hl=en
title: https://developer.chrome.com/blog/memory-safety-fonts?hl=en
date: 2025-05-11T16:56:47.746056
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/memory-safety-fonts?hl=es-419)




  * On this page
  * [Why replace FreeType?](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#why_replace_freetype)
    * [Why issues keep sneaking in](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#why_issues_keep_sneaking_in)
  * [Skrifa in Chrome](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#skrifa_in_chrome)
    * [Safety, first and foremost](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#safety_first_and_foremost)
    * [Correctness matters](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#correctness_matters)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Memory safety for web fonts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Why replace FreeType?](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#why_replace_freetype)
    * [Why issues keep sneaking in](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#why_issues_keep_sneaking_in)
  * [Skrifa in Chrome](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#skrifa_in_chrome)
    * [Safety, first and foremost](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#safety_first_and_foremost)
    * [Correctness matters](https://developer.chrome.com/blog/memory-safety-fonts?hl=en#correctness_matters)


Dominik Röttsches 
[ GitHub ](https://github.com/drott) [ Mastodon ](https://typo.social/@drott)
Rod Sheeter 
[ GitHub ](https://github.com/rsheeter)
Chad Brokaw 
[ GitHub ](https://github.com/dfrg)
Published: March 19, 2025 
[Skrifa](https://github.com/googlefonts/fontations/tree/main/skrifa) is written in Rust, and created as a replacement for FreeType to make font processing in Chrome secure for all our users. Skrifa takes advantage of Rust's memory safety, and lets us iterate faster on font technology improvements in Chrome. Moving from FreeType to Skrifa allows us to be both agile and fearless when making changes to our font code. We now spend far less time fixing security bugs, resulting in faster updates, and better code quality.
This post shares why Chrome has moved away from FreeType, and some interesting technical details of the improvements this move has enabled.
## Why replace FreeType?
The web is unique in that it allows users to fetch untrusted resources from a wide variety of untrusted sources with the expectation that things will just work, and that they are safe in doing so. This assumption is generally correct, but keeping that promise to users comes at a cost. For example, to use a web font safely (a font delivered over the network) Chrome employs several security mitigations:
  * Font processing is [sandboxed](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md) per the [rule of two](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md): they are untrustworthy and the consuming code is unsafe.
  * Fonts are passed through the [OpenType Sanitizer](https://github.com/khaledhosny/ots) prior to processing.
  * All the libraries involved in decompressing and processing fonts are [fuzz tested](https://en.wikipedia.org/wiki/Fuzzing).


Chrome ships with FreeType and makes use of it as the primary font processing library on Android, ChromeOS, and Linux. That means a **lot** of users are exposed if there is a vulnerability in FreeType.
The FreeType library is used by Chrome to compute metrics and load hinted outlines from fonts. Overall, use of FreeType has been a huge win for Google. It does a complex job, and does it well, we rely on it extensively and contribute back to it. However, it is written in unsafe code and has its origins in a time when malicious inputs were less likely. Merely keeping up with the stream of issues found by fuzzing costs Google at least 0.25 full time software engineers. Worse, we observably don't find everything or find things only after the code has shipped to users.
This pattern of problems is not unique to FreeType, we observe that other unsafe libraries admit issues even when we use the best software engineers we can find, code review every change, and require tests.
### Why issues keep sneaking in
When we evaluated FreeType's security, we observed three main classes of issue to occur (non-exhaustive):
#### Use of an unsafe language
Pattern/Issue | Example  
---|---  
Manual memory management | 
  * [CVE-2014-9661](https://nvd.nist.gov/vuln/detail/CVE-2014-9661), use after free, identified by Project Zero, [Project Zero tracker](https://project-zero.issues.chromium.org/issues/42450955)


  * [CVE-2020-15999](https://nvd.nist.gov/vuln/detail/cve-2020-15999), heap overflow identified to be [actively exploited](https://googleprojectzero.blogspot.com/2021/03/in-wild-series-october-2020-0-day.html) by Project Zero

  
Unchecked array access  
Integer overflows | During execution of embedded virtual machines for TrueType hinting of CFF drawing and hinting <https://issues.oss-fuzz.com/issues?q=FreeType%20Integer-overflow>  
Incorrect use of zeroing versus non-zeroing allocation | Discussion in <https://gitlab.freedesktop.org/freetype/freetype/-/merge_requests/94>, [8 fuzzer issues found](http://issues.chromium.org/issues?q=id:\(40055682%20%7C%2040055692%20%7C%2040057647%20%7C%2040057647%20%7C%2040057653%20%7C%2040057656%20%7C%2040057666%20%7C%2040057667\)) afterwards   
Invalid casts | See the following row on macro usage  
#### Project specific issues
Pattern/Issue | Example  
---|---  
Macros obscure lack of explicit size typing | 
  * Macros such as `FT_READ_*` and `FT_PEEK_*` obscure what integer types are being used, hiding that C99 types with explicit sizes (int16_t, etc) are not used


  * [Fix reading s32 when long is s64](https://gitlab.freedesktop.org/freetype/freetype/-/merge_requests/175)

  
New code consistently adds bugs, even when written defensively. | 
  * COLRv1 and OT-SVG support both produced issues


  * Fuzzing finds some, but not necessarily all, [#32421](https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=32421), [#52404](https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=52404)

  
Lack of tests | 
  * Crafting test fonts is time consuming and difficult


  * For example, the [fix](https://gitlab.freedesktop.org/freetype/freetype/-/commit/a3bab162b2ae616074c8877a04556932998aeacd) for [CVE-2020-15999](https://nvd.nist.gov/vuln/detail/cve-2020-15999) adds no test 

  
#### Dependency issues
Fuzzing has repeatedly identified issues in libraries FreeType depends on, such as bzip2, libpng, and zlib. As an example, compare [freetype_bdf_fuzzer: Use-of-uninitialized-value in inflate](https://issues.chromium.org/issues/40055682).
#### Fuzzing isn't enough
Fuzzing–automated testing with a wide range of inputs, including randomized invalid ones–is meant to find many of the types of issues that get into the stable release of Chrome. We fuzz FreeType as part of Google's [oss-fuzz](https://github.com/google/oss-fuzz) project. It does find issues, but fonts have proven somewhat resistant to fuzzing, for the following reasons.
Font files are complex, comparable to video files as they contain multiple different types of information. Font files are a container format for multiple tables, where each table serves a different purpose in processing text and fonts together to produce a correctly positioned glyph on the screen. In a font file you will find:
  * Static metadata such as font names and parameters for variable fonts.
  * Mappings from Unicode characters to glyphs.
  * A complex ruleset and grammar for screen layout of glyphs.
  * Visual information: Glyph shapes and image information describing what the glyphs placed on the screen look like. 
    * The visual tables can in turn include TrueType hinting programs, which are mini programs executed to change the glyph shape.
    * Char strings in the CFF or CFF2 tables which are imperative curve drawing and hinting instructions executed in the CFF rendering engine.


There is complexity in font files equivalent to having its own programming language and state machine processing, requiring specific virtual machines to execute them.
Because of the complexity of the format, fuzzing has shortcomings in finding issues in font files.
Good code coverage or fuzzer progress is difficult to achieve for the following reasons:
  * Fuzzing TrueType hinting programs, CFF char strings and OpenType layout using simple bit-flipping/shift/insertion/deletion-style mutators struggles to reach all combinations of states.
  * Fuzzing needs to at least produce partially valid structures. Random mutation rarely does so, making good coverage hard to achieve, particularly for deeper levels of code.
  * The current fuzzing efforts in ClusterFuzz and oss-fuzz are not yet using structure-aware mutation. Use of grammar- or structure-aware mutators might help avoid production of variants that are rejected early, at the cost of taking more time to develop, and introducing chances which miss parts of the search space.


Data in multiple tables needs to be in sync for fuzzing to make progress:
  * The usual mutation patterns of fuzzers don't produce partially valid data so many iterations get rejected and progress becomes slow.
  * The glyph mapping, the OpenType layout tables and glyph drawing are connected and depend on each other, forming a combinatorial space whose corners are hard to reach with fuzzing.
  * For example, the high-severity [tt_face_get_paint COLRv1](https://issues.chromium.org/40055587) vulnerability took more than 10 months to find.


Despite our best efforts, font security issues have repeatedly reached end users. Replacing FreeType with a Rust alternative will prevent multiple entire classes of vulnerability.
## Skrifa in Chrome
[Skia](https://skia.org/) is the graphics library used by Chrome. Skia relies on FreeType to load metadata and letterforms from fonts. [Skrifa](https://github.com/googlefonts/fontations/tree/main/skrifa) is a Rust library, part of the [Fontations](https://github.com/googlefonts/fontations) family of libraries, that provides a safe replacement for the parts of FreeType used by Skia.
To transition FreeType to Skia the Chrome team developed a new Skia font backend based on [Skrifa](https://github.com/googlefonts/fontations/tree/main/skrifa) and gradually rolled out the change to users:
  * In [Chrome 128 (August 2024) we enabled Fontations](https://chromiumdash.appspot.com/commit/6df58d58e667f19490acc1c51095aaf08842bea7) for use in less commonly used font formats, such as for color fonts and CFF2, as a safe trial run.
  * In [Chrome 133 (February 2025) we enabled Fontations](https://chromestatus.com/feature/5717358869217280) for all web fonts usage on Linux, Android and ChromeOS, and for web fonts usage as fallback on Windows and Mac—in cases where the system does not support a font format but Chrome needs to display it.


For the integration into Chrome, we rely on the smooth integration of Rust into the codebase introduced by the [Chrome security team](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html).
In the future we'll switch to Fontations for operating system fonts as well, starting with Linux and ChromeOS, then on Android.
### Safety, first and foremost
Our primary goal is to reduce (or ideally, eliminate!) security vulnerabilities that are caused by out of bounds access to memory. Rust provides this out of the box as long as you avoid any _unsafe_ code blocks.
Our performance goals require us to perform one operation that is currently unsafe: reinterpretation of arbitrary bytes as a strongly typed data structure. This allows us to read the data from a font file without performing [unnecessary copies](https://en.wikipedia.org/wiki/Zero-copy) and is essential for producing a fast font parser.
To avoid our own unsafe code, we've chosen to outsource this responsibility to [bytemuck](https://crates.io/crates/bytemuck) which is a Rust library designed specifically for this purpose and is widely tested and used across the ecosystem. Concentrating raw data reinterpretation in bytemuck ensures we have this functionality in one place and audited, and avoid repeating unsafe code for the purpose. The [safe transmute project](https://rust-lang.github.io/rfcs/2835-project-safe-transmute.html) aims to incorporate this functionality directly into the Rust compiler and we will make the switch as soon as it is available.
### Correctness matters
Skrifa is built out of independent components where most data structures are designed to be immutable. This improves readability, maintainability and multithreading. It also makes the code more amenable to unit testing. We've taken advantage of this opportunity and have produced a suite of roughly 700 unit tests that cover our full stack from low level parsing routines to high level hinting virtual machines.
Correctness also implies fidelity and FreeType is highly regarded for its generation of high quality outlines. We must match this quality to be a suitable replacement. To that end, we have built a bespoke tool called [fauntlet](https://github.com/googlefonts/fontations/tree/main/fauntlet) that compares the output of Skrifa and FreeType for batches of font files across a wide range of configurations. This affords us some assurance that we can avoid regressions in quality.
In addition, before the integration into Chromium, we ran a [wide set of pixel comparisons](https://source.chromium.org/chromium/chromium/src/+/main:third_party/skia/gm/fontations_ft_compare.cpp) in Skia, comparing FreeType rendering to Skrifa and Skia rendering to ensure the pixel differences are absolutely minimal, in all required rendering modes (across different antialiasing and hinting modes).
[Fuzz testing](https://en.wikipedia.org/wiki/Fuzzing) is an important tool for determining how a piece of software will react to malformed and malicious inputs. We've been continuously fuzzing our new code since June of 2024. This covers the Rust libraries itself and the integration code. While the fuzzer has found (as of this writing) 39 bugs, it's worth noting that **none of these have been security critical**. They may cause undesired visual results or even controlled crashes, but won't lead to exploitable vulnerabilities.
## Onward!
We are very pleased with the results of our efforts to use Rust for text. Delivering safer code to users _and_ gaining developer productivity is a huge win for us. We plan to continue to seek opportunities to use Rust in our text stacks. If you'd like to know more, [Oxidize](https://github.com/googlefonts/oxidize) outlines some of Google Fonts future plans.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-19 UTC.

