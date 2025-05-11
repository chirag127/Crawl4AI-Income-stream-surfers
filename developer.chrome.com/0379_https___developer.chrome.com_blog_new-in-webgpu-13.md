---
url: https://developer.chrome.com/blog/new-in-webgpu-132?hl=en
title: https://developer.chrome.com/blog/new-in-webgpu-132?hl=en
date: 2025-05-11T17:54:32.059503
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-webgpu-132?hl=es-419)




  * On this page
  * [Texture view usage](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#texture_view_usage)
  * [32-bit float textures blending](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#32-bit_float_textures_blending)
  * [GPUDevice adapterInfo attribute](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#gpudevice_adapterinfo_attribute)
  * [Configuring canvas context with invalid format throw JavaScript error](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#configuring_canvas_context_with_invalid_format_throw_javascript_error)
  * [Filtering sampler restrictions on textures](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#filtering_sampler_restrictions_on_textures)
  * [Extended subgroups experimentation](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#extended_subgroups_experimentation)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#improving_developer_experience)
  * [Experimental support for 16-bit normalized texture formats](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#experimental_support_for_16-bit_normalized_texture_formats)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#whats-new)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's New in WebGPU (Chrome 132) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Texture view usage](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#texture_view_usage)
  * [32-bit float textures blending](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#32-bit_float_textures_blending)
  * [GPUDevice adapterInfo attribute](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#gpudevice_adapterinfo_attribute)
  * [Configuring canvas context with invalid format throw JavaScript error](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#configuring_canvas_context_with_invalid_format_throw_javascript_error)
  * [Filtering sampler restrictions on textures](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#filtering_sampler_restrictions_on_textures)
  * [Extended subgroups experimentation](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#extended_subgroups_experimentation)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#improving_developer_experience)
  * [Experimental support for 16-bit normalized texture formats](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#experimental_support_for_16-bit_normalized_texture_formats)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-132?hl=en#whats-new)


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
Published: January 8, 2025 
## Texture view usage
GPU texture views currently inherit all usage flags from their source GPU texture. This can be problematic as some view formats are incompatible with certain usages. To address this issue, calling [`createView()`](https://developer.mozilla.org/docs/Web/API/GPUTexture/createView) with the optional [`usage`](https://gpuweb.github.io/gpuweb/#dom-gputextureviewdescriptor-usage) member lets you explicitly specify a subset of the source texture's usage flags that are compatible with the chosen view format.
This change allows for upfront validation and more fine-grained control over how the view is used. It also aligns with other graphics APIs where usage flags are common parameters in view creation, offering optimization opportunities.
See the following snippet, the [chromestatus entry](https://chromestatus.com/feature/5155252832305152), and [issue 363903526](https://issues.chromium.org/issues/363903526).
```
consttexture=myDevice.createTexture({
size:[4,4],
format:"rgba8unorm",
usage:
GPUTextureUsage.RENDER_ATTACHMENT|
GPUTextureUsage.TEXTURE_BINDING|
GPUTextureUsage.STORAGE_BINDING,
viewFormats:["rgba8unorm-srgb"],
});
constview=texture.createView({
format:'rgba8unorm-srgb',
usage:GPUTextureUsage.RENDER_ATTACHMENT,// Restrict allowed usage.
});

```

## 32-bit float textures blending
32-bit floating-point textures are essential for HDR rendering to preserve a wide range of color values and prevent color banding artifacts. For example in scientific visualization.
The new [`"float32-blendable"`](https://gpuweb.github.io/gpuweb/#float32-blendable) GPU feature makes GPU textures with formats `"r32float"`, `"rg32float"`, and `"rgba32float"` blendable. Creating a render pipeline that uses blending with any float32-format attachment is now possible when requesting a GPU device with this feature.
See the following snippet, the [chromestatus entry](https://chromestatus.com/feature/5173655901044736), and [issue 369649348](https://issues.chromium.org/issues/369649348).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(!adapter.features.has("float32-blendable")){
thrownewError("32-bit float textures blending support is not available");
}
// Explicitly request 32-bit float textures blending support.
constdevice=awaitadapter.requestDevice({
requiredFeatures:["float32-blendable"],
});
// ... Creation of shader modules is omitted for readability.
// Create a render pipeline that uses blending for the rgba32float format.
device.createRenderPipeline({
vertex:{module:myVertexShaderModule},
fragment:{
module:myFragmentShaderModule,
targets:[
{
format:"rgba32float",
blend:{color:{},alpha:{}},
},
],
},
layout:"auto",
});
// Create the GPU texture with rgba32float format and
// send the appropriate commands to the GPU...

```

## GPUDevice `adapterInfo` attribute
It's important for libraries that take user-provided `GPUDevice` objects to access information about the physical GPU, as they may need to optimize or implement workarounds based on the GPU architecture. While it is possible to access to this information through the `GPUAdapter` object, there is no direct way to get it from a `GPUDevice` alone. This can be inconvenient, as it may require users to provide additional information alongside the `GPUDevice`.
To address this problem, [`GPUAdapterInfo`](https://developer.mozilla.org/docs/Web/API/GPUAdapterInfo) is now exposed through the `GPUDevice` [`adapterInfo`](https://gpuweb.github.io/gpuweb/#dom-gpudevice-adapterinfo) attribute. Those are similar to the existing `GPUAdapter` [`info`](https://developer.mozilla.org/docs/Web/API/GPUAdapter/info) attribute.
See the following snippet, the [chromestatus entry](https://chromestatus.com/feature/6221851301511168), and [issue 376600838](https://issues.chromium.org/issues/376600838).
```
functionoptimizeForGpuDevice(device){
if(device.adapterInfo.vendor==="amd"){
// Use AMD-specific optimizations.
}elseif(device.adapterInfo.architecture.includes("turing")){
// Optimize for NVIDIA Turing architecture.
}
}

```

## Configuring canvas context with invalid format throw JavaScript error
Previously, using an invalid texture format with the [`configure()`](https://developer.mozilla.org/docs/Web/API/GPUCanvasContext/configure) method of the GPU canvas context resulted in a GPU validation error. This has been changed to throw a JavaScript `TypeError`. This prevents scenarios where [`getCurrentTexture()`](https://developer.mozilla.org/docs/Web/API/GPUCanvasContext/getCurrentTexture) returns a valid GPU texture despite the GPU canvas context being configured incorrectly. More information can be found in [issue 372837859](https://issues.chromium.org/issues/372837859).
## Filtering sampler restrictions on textures
Using `"sint"`, `"uint"`, and "`depth"` format textures with filtering samples was allowed previously. It now correctly disallows using an `"sint"` or `"uint"` format texture with a filtering sampler. Note that it currently emits a warning if you use a "`depth"` texture with a filtering sampler as it will be disallowed in the future. See [issue 376497143](https://issues.chromium.org/issues/376497143).
Those restrictions means using a depth texture with a non-filtering sampler requires manual creation of bind group layouts. This is because the "auto" generated bind group layouts don't support this combination yet. [Spec issue 4952](https://github.com/gpuweb/gpuweb/issues/4952) contains a proposal under consideration to address this limitation in the future.
## Extended subgroups experimentation
The [subgroups experimentation](https://developer.chrome.com/blog/new-in-webgpu-128#experimenting_with_subgroups), initially set to end in Chrome 131, has been extended to Chrome 133, concluding on April 16, 2025. While the first origin trial focused on performance, it lacked crucial [portability safeguards](https://github.com/gpuweb/gpuweb/pull/4963). These safeguards will now be added, potentially causing errors in existing code.
## Improving developer experience
A warning is now visible in DevTools when the `powerPreference` option is used with [`requestAdapter()`](https://developer.mozilla.org/docs/Web/API/GPU/requestAdapter) on Windows. This warning will be removed when Chrome knows how to use two different GPUs and composite the results between them. See [issue 369219127](https://issues.chromium.org/issues/369219127).
The size of the GPU buffer is now present in the error message when creating a GPU buffer that is too large. See [issue 374167798](https://issues.chromium.org/issues/374167798).
## Experimental support for 16-bit normalized texture formats
16-bit signed normalized and unsigned normalized texture formats are now available experimentally respectively behind the `"chromium-experimental-snorm16-texture-formats"` and `"chromium-experimental-unorm16-texture-formats"` GPU features while they're being [discussed for standardization](https://github.com/gpuweb/gpuweb/issues/3001).
These features add support for 16-bit normalized texture formats with `COPY_SRC`, `COPY_DST`, `TEXTURE_BINDING`, `RENDER_ATTACHMENT` usages, multisampling, and resolving capabilities. The additional formats are `"r16unorm"`, `"rg16unorm"`, `"rgba16unorm"`, `"r16snorm"`, `"rg16snorm"`, and `"rgba16snorm"`.
Until these experimental features are standardized, enable the "Unsafe WebGPU Support" flag at `chrome://flags/#enable-unsafe-webgpu` to make them available in Chrome.
See the following snippet and [issue 374790898](https://issues.chromium.org/issues/374790898).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(!adapter.features.has("chromium-experimental-snorm16-texture-formats")){
thrownewError("16-bit signed normalized formats support is not available");
}
// Explicitly request 16-bit signed normalized formats support.
constdevice=awaitadapter.requestDevice({
requiredFeatures:["chromium-experimental-snorm16-texture-formats"],
});
// Create a texture with the rgba16snorm format which consists of four
// components, each of which is a 16-bit, normalized, signed integer value.
consttexture=device.createTexture({
size:[4,4],
format:"rgba16snorm",
usage:GPUTextureUsage.RENDER_ATTACHMENT|GPUTextureUsage.TEXTURE_BINDING,
});
// Send the appropriate commands to the GPU...

```

## Dawn updates
The `EnumerateFeatures(FeatureName * features)` methods from `wgpu::Adapter` and `wgpu::Device` are deprecated in favor of using `GetFeatures(SupportedFeatures * features)`. See [issue 368672123](https://issues.chromium.org/issues/368672123).
The webgpu.h C API has changed all `char const *` to a [`WGPUStringView`](https://webgpu-native.github.io/webgpu-headers/Strings.html) structure that defines a view into a UTF-8 encoded string. It acts like a pointer to the string's data, coupled with a length. This lets you work with parts of a string without needing to copy it. See [issue 42241188](https://issues.chromium.org/issues/42241188).
This covers only some of the key highlights. Check out the exhaustive [list of commits](https://dawn.googlesource.com/dawn/+log/chromium/6778..chromium/6834?n=1000).
## What's New in WebGPU
A list of everything that has been covered in the [What's New in WebGPU](https://developer.chrome.com/docs/web-platform/webgpu/news) series.
### Chrome 136
  * [GPUAdapterInfo isFallbackAdapter attribute](https://developer.chrome.com/blog/new-in-webgpu-136#gpuadapterinfo_isfallbackadapter_attribute)
  * [Shader compilation time improvements on D3D12](https://developer.chrome.com/blog/new-in-webgpu-136#shader_compilation_time_improvements_on_d3d12)
  * [Save and copy canvas images](https://developer.chrome.com/blog/new-in-webgpu-136#save_and_copy_canvas_images)
  * [Lift compatibility mode restrictions](https://developer.chrome.com/blog/new-in-webgpu-136#lift_compatibility_mode_restrictions)


### Chrome 135
  * [Allow creating pipeline layout with null bind group layout](https://developer.chrome.com/blog/new-in-webgpu-135#allow_creating_pipeline_layout_with_null_bind_group_layout)
  * [Allow viewports to extend past the render targets bounds](https://developer.chrome.com/blog/new-in-webgpu-135#allow_viewports_to_extend_past_the_render_targets_bounds)
  * [Easier access to the experimental compatibility mode on Android](https://developer.chrome.com/blog/new-in-webgpu-135#easier_access_to_the_experimental_compatibility_mode_on_android)
  * [Remove maxInterStageShaderComponents limit](https://developer.chrome.com/blog/new-in-webgpu-135#remove_maxinterstageshadercomponents_limit)


### Chrome 134
  * [Improve machine-learning workloads with subgroups](https://developer.chrome.com/blog/new-in-webgpu-134#improve_machine-learning_workloads_with_subgroups)
  * [Remove float filterable texture types support as blendable](https://developer.chrome.com/blog/new-in-webgpu-134#remove_float_filterable_texture_types_support_as_blendable)


### Chrome 133
  * [Additional unorm8x4-bgra and 1-component vertex formats](https://developer.chrome.com/blog/new-in-webgpu-133#additional_unorm8x4-bgra_and_1-component_vertex_formats)
  * [Allow unknown limits to be requested with undefined value](https://developer.chrome.com/blog/new-in-webgpu-133#allow_unknown_limits_to_be_requested_with_undefined_value)
  * [WGSL alignment rules changes](https://developer.chrome.com/blog/new-in-webgpu-133#wgsl_alignment_rules_changes)
  * [WGSL performance gains with discard](https://developer.chrome.com/blog/new-in-webgpu-133#wgsl_performance_gains_with_discard)
  * [Use VideoFrame displaySize for external textures](https://developer.chrome.com/blog/new-in-webgpu-133#use_videoframe_displaysize_for_external_textures)
  * [Handle images with non-default orientations using copyExternalImageToTexture](https://developer.chrome.com/blog/new-in-webgpu-133#handle_images_with_non-default_orientations_using_copyexternalimagetotexture)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-133#improving_developer_experience)
  * [Enable compatibility mode with featureLevel](https://developer.chrome.com/blog/new-in-webgpu-133#enable_compatibility_mode_with_featurelevel)
  * [Experimental subgroup features cleanup](https://developer.chrome.com/blog/new-in-webgpu-133#experimental_subgroup_features_cleanup)
  * [Deprecate maxInterStageShaderComponents limit](https://developer.chrome.com/blog/new-in-webgpu-133#deprecate_maxinterstageshadercomponents_limit)


### Chrome 132
  * [Texture view usage](https://developer.chrome.com/blog/new-in-webgpu-132#texture_view_usage)
  * [32-bit float textures blending](https://developer.chrome.com/blog/new-in-webgpu-132#32-bit_float_textures_blending)
  * [GPUDevice adapterInfo attribute](https://developer.chrome.com/blog/new-in-webgpu-132#gpudevice_adapterinfo_attribute)
  * [Configuring canvas context with invalid format throw JavaScript error](https://developer.chrome.com/blog/new-in-webgpu-132#configuring_canvas_context_with_invalid_format_throw_javascript_error)
  * [Filtering sampler restrictions on textures](https://developer.chrome.com/blog/new-in-webgpu-132#filtering_sampler_restrictions_on_textures)
  * [Extended subgroups experimentation](https://developer.chrome.com/blog/new-in-webgpu-132#extended_subgroups_experimentation)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-132#improving_developer_experience)
  * [Experimental support for 16-bit normalized texture formats](https://developer.chrome.com/blog/new-in-webgpu-132#experimental_support_for_16-bit_normalized_texture_formats)


### Chrome 131
  * [Clip distances in WGSL](https://developer.chrome.com/blog/new-in-webgpu-131#clip_distances_in_wgsl)
  * [GPUCanvasContext getConfiguration()](https://developer.chrome.com/blog/new-in-webgpu-131#gpucanvascontext_getconfiguration)
  * [Point and line primitives must not have depth bias](https://developer.chrome.com/blog/new-in-webgpu-131#point_and_line_primitives_must_not_have_depth_bias)
  * [Inclusive scan built-in functions for subgroups](https://developer.chrome.com/blog/new-in-webgpu-131#inclusive_scan_built-in_functions_for_subgroups)
  * [Experimental support for multi-draw indirect](https://developer.chrome.com/blog/new-in-webgpu-131#experimental_support_for_multi-draw_indirect)
  * [Shader module compilation option strict math](https://developer.chrome.com/blog/new-in-webgpu-131#shader_module_compilation_option_strict_math)
  * [Remove GPUAdapter requestAdapterInfo()](https://developer.chrome.com/blog/new-in-webgpu-131#remove_gpuadapter_requestadapterinfo)


### Chrome 130
  * [Dual source blending](https://developer.chrome.com/blog/new-in-webgpu-130#dual_source_blending)
  * [Shader compilation time improvements on Metal](https://developer.chrome.com/blog/new-in-webgpu-130#shader_compilation_time_improvements_on_metal)
  * [Deprecation of GPUAdapter requestAdapterInfo()](https://developer.chrome.com/blog/new-in-webgpu-130#deprecation_of_gpuadapter_requestadapterinfo)


### Chrome 129
  * [HDR support with canvas tone mapping mode](https://developer.chrome.com/blog/new-in-webgpu-129#hdr_support_with_canvas_tone_mapping_mode)
  * [Expanded subgroups support](https://developer.chrome.com/blog/new-in-webgpu-129#expanded_subgroups_support)


### Chrome 128
  * [Experimenting with subgroups](https://developer.chrome.com/blog/new-in-webgpu-128#experimenting_with_subgroups)
  * [Deprecate setting depth bias for lines and points](https://developer.chrome.com/blog/new-in-webgpu-128#deprecate_setting_depth_bias_for_lines_and_points)
  * [Hide uncaptured error DevTools warning if preventDefault](https://developer.chrome.com/blog/new-in-webgpu-128#hide_uncaptured_error_devtools_warning_if_preventdefault)
  * [WGSL interpolate sampling first and either](https://developer.chrome.com/blog/new-in-webgpu-128#wgsl_interpolate_sampling_first_and_either)


### Chrome 127
  * [Experimental support for OpenGL ES on Android](https://developer.chrome.com/blog/new-in-webgpu-127#experimental_support_for_opengl_es_on_android)
  * [GPUAdapter info attribute](https://developer.chrome.com/blog/new-in-webgpu-127#gpuadapter_info_attribute)
  * [WebAssembly interop improvements](https://developer.chrome.com/blog/new-in-webgpu-127#webassembly_interop_improvements)
  * [Improved command encoder errors](https://developer.chrome.com/blog/new-in-webgpu-127#improved_command_encoder_errors)


### Chrome 126
  * [Increase maxTextureArrayLayers limit](https://developer.chrome.com/blog/new-in-webgpu-126#increase_maxtexturearraylayers_limit)
  * [Buffer upload optimization for Vulkan backend](https://developer.chrome.com/blog/new-in-webgpu-126#buffer_upload_optimization_for_vulkan_backend)
  * [Shader compilation time improvements](https://developer.chrome.com/blog/new-in-webgpu-126#shader_compilation_time_improvements)
  * [Submitted command buffers must be unique](https://developer.chrome.com/blog/new-in-webgpu-126#submitted_command_buffers_must_be_unique)


### Chrome 125
  * [Subgroups (feature in development)](https://developer.chrome.com/blog/new-in-webgpu-125#subgroups_feature_in_development)
  * [Render to slice of 3D texture](https://developer.chrome.com/blog/new-in-webgpu-125#render_to_slice_of_3d_texture)


### Chrome 124
  * [Read-only and read-write storage textures](https://developer.chrome.com/blog/new-in-webgpu-124#read-only_and_read-write_storage_textures)
  * [Service workers and shared workers support](https://developer.chrome.com/blog/new-in-webgpu-124#service_workers_and_shared_workers_support)
  * [New adapter information attributes](https://developer.chrome.com/blog/new-in-webgpu-124#new_adapter_information_attributes)


### Chrome 123
  * [DP4a built-in functions support in WGSL](https://developer.chrome.com/blog/new-in-webgpu-123#dp4a_built-in_functions_support_in_wgsl)
  * [Unrestricted pointer parameters in WGSL](https://developer.chrome.com/blog/new-in-webgpu-123#unrestricted_pointer_parameters_in_wgsl)
  * [Syntax sugar for dereferencing composites in WGSL](https://developer.chrome.com/blog/new-in-webgpu-123#syntax_sugar_for_dereferencing_composites_in_wgsl)
  * [Separate read-only state for stencil and depth aspects](https://developer.chrome.com/blog/new-in-webgpu-123#separate_read-only_state_for_stencil_and_depth_aspects)


### Chrome 122
  * [Expand reach with compatibility mode (feature in development)](https://developer.chrome.com/blog/new-in-webgpu-122#expand_reach_with_compatibility_mode_feature_in_development)
  * [Increase maxVertexAttributes limit](https://developer.chrome.com/blog/new-in-webgpu-122#increase_maxvertexattributes_limit)


### Chrome 121
  * [Support WebGPU on Android](https://developer.chrome.com/blog/new-in-webgpu-121#support-webgpu-on-android)
  * [Use DXC instead of FXC for shader compilation on Windows](https://developer.chrome.com/blog/new-in-webgpu-121#use_dxc_instead_of_fxc_for_shader_compilation_on_windows)
  * [Timestamp queries in compute and render passes](https://developer.chrome.com/blog/new-in-webgpu-121#timestamp_queries_in_compute_and_render_passes)
  * [Default entry points to shader modules](https://developer.chrome.com/blog/new-in-webgpu-121#default_entry_points_to_shader_modules)
  * [Support display-p3 as GPUExternalTexture color space](https://developer.chrome.com/blog/new-in-webgpu-121#support_display-p3_as_gpuexternaltexture_color_space)
  * [Memory heaps info](https://developer.chrome.com/blog/new-in-webgpu-121#memory_heaps_info)


### Chrome 120
  * [Support for 16-bit floating-point values in WGSL](https://developer.chrome.com/blog/new-in-webgpu-120#support_for_16-bit_floating-point_values_in_wgsl)
  * [Changes to depth-stencil state](https://developer.chrome.com/blog/new-in-webgpu-120#changes_to_depth-stencil_state)
  * [Adapter information updates](https://developer.chrome.com/blog/new-in-webgpu-120#adapter_information_updates)
  * [Timestamp queries quantization](https://developer.chrome.com/blog/new-in-webgpu-120#timestamp_queries_quantization)
  * [Spring-cleaning features](https://developer.chrome.com/blog/new-in-webgpu-120#spring-cleaning_features)


### Chrome 119
  * [Filterable 32-bit float textures](https://developer.chrome.com/blog/new-in-webgpu-119#filterable_32-bit_float_textures)
  * [unorm10-10-10-2 vertex format](https://developer.chrome.com/blog/new-in-webgpu-119#unorm10-10-10-2_vertex_format)
  * [rgb10a2uint texture format](https://developer.chrome.com/blog/new-in-webgpu-119#rgb10a2uint_texture_format)


### Chrome 118
  * [HTMLImageElement and ImageData support in `copyExternalImageToTexture()`](https://developer.chrome.com/blog/new-in-webgpu-118#htmlimageelement_and_imagedata_support_in_copyexternalimagetotexture)
  * [Experimental support for read-write and read-only storage texture](https://developer.chrome.com/blog/new-in-webgpu-118#experimental_support_for_read-write_and_read-only_storage_texture)


### Chrome 117
  * [Unset vertex buffer](https://developer.chrome.com/blog/new-in-webgpu-117#unset_vertex_buffer)
  * [Silence errors from async pipeline creation when device is lost](https://developer.chrome.com/blog/new-in-webgpu-117#silence_errors_from_async_pipeline_creation_when_device_is_lost)
  * [SPIR-V shader module creation updates](https://developer.chrome.com/blog/new-in-webgpu-117#spir-v_shader_module_creation_updates)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-117#improving_developer_experience)
  * [Caching pipelines with automatically generated layout](https://developer.chrome.com/blog/new-in-webgpu-117#caching_pipelines_with_automatically_generated_layout)


### Chrome 116
  * [WebCodecs integration](https://developer.chrome.com/blog/new-in-webgpu-116#webcodecs_integration)
  * [Lost device returned by GPUAdapter `requestDevice()`](https://developer.chrome.com/blog/new-in-webgpu-116#lost_device_returned_by_gpuadapter_requestdevice)
  * [Keep video playback smooth if `importExternalTexture()` is called](https://developer.chrome.com/blog/new-in-webgpu-116#keep_video_playback_smooth_if_importexternaltexture_is_called)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-116#improving_developer_experience)


### Chrome 115
  * [Supported WGSL language extensions](https://developer.chrome.com/blog/new-in-webgpu-115#supported_wgsl_language_extensions)
  * [Experimental support for Direct3D 11](https://developer.chrome.com/blog/new-in-webgpu-115#experimental_support_for_direct3d_11)
  * [Get discrete GPU by default on AC power](https://developer.chrome.com/blog/new-in-webgpu-115#get_discrete_gpu_by_default_on_ac_power)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-115#improving_developer_experience)


### Chrome 114
  * [Optimize JavaScript](https://developer.chrome.com/blog/new-in-webgpu-114#optimize_javascript)
  * [getCurrentTexture() on unconfigured canvas throws InvalidStateError](https://developer.chrome.com/blog/new-in-webgpu-114#getcurrenttexture_on_unconfigured_canvas_throws_invalidstateerror)


### Chrome 113
  * [Use WebCodecs VideoFrame source in `importExternalTexture()`](https://developer.chrome.com/blog/new-in-webgpu-113#use_webcodecs_videoframe_source_in_importexternaltexture)


Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-01-08 UTC.

