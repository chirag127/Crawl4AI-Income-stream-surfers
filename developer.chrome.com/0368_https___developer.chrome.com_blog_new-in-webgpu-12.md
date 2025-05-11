---
url: https://developer.chrome.com/blog/new-in-webgpu-120?hl=en
title: https://developer.chrome.com/blog/new-in-webgpu-120?hl=en
date: 2025-05-11T17:54:16.468512
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-webgpu-120?hl=es-419)




  * On this page
  * [Support for 16-bit floating-point values in WGSL](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#support_for_16-bit_floating-point_values_in_wgsl)
  * [Changes to depth-stencil state](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#changes_to_depth-stencil_state)
  * [Adapter information updates](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#adapter_information_updates)
  * [Timestamp queries quantization](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#timestamp_queries_quantization)
  * [Spring-cleaning features](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#spring-cleaning_features)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#whats-new)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's New in WebGPU (Chrome 120) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Support for 16-bit floating-point values in WGSL](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#support_for_16-bit_floating-point_values_in_wgsl)
  * [Changes to depth-stencil state](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#changes_to_depth-stencil_state)
  * [Adapter information updates](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#adapter_information_updates)
  * [Timestamp queries quantization](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#timestamp_queries_quantization)
  * [Spring-cleaning features](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#spring-cleaning_features)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-120?hl=en#whats-new)


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
## Support for 16-bit floating-point values in WGSL
In WGSL, the [`f16` type](https://www.w3.org/TR/WGSL/#f16) is the set of 16-bit floating-point values of the IEEE-754 binary16 (half precision) format. It means that it uses 16 bits to represent a floating-point number, as opposed to 32 bits for conventional single-precision floating-point ([`f32`](https://gpuweb.github.io/gpuweb/wgsl/#f32)). This smaller size can lead to significant [performance improvements](https://therealmjp.github.io/posts/shader-fp16/), especially when processing large amounts of data.
For comparison, on an Apple M1 Pro device, the `f16` implementation of [Llama2 7B models](https://huggingface.co/meta-llama/Llama-2-7b) used in the [WebLLM chat demo](https://webllm.mlc.ai/#chat-demo) is significantly faster than the `f32` implementation, with a 28% improvement in prefill speed and a 41% improvement in decoding speed as shown in the following screenshots.
WebLLM chat demos with `f32` (left) and `f16` (right) Llama2 7B models.
Not all GPUs support 16-bit floating-point values. When the [`"shader-f16"`](https://gpuweb.github.io/gpuweb/#shader-f16) feature is available in a `GPUAdapter`, you can now request a `GPUDevice` with this feature and create a WGSL shader module that takes advantage of the half-precision floating-point type `f16`. This type is valid to use in the WGSL shader module only if you enable the [`f16` WGSL extension](https://gpuweb.github.io/gpuweb/wgsl/#extension-f16) with `enable f16;`. Otherwise, [createShaderModule()](https://developer.mozilla.org/en-US/docs/Web/API/GPUDevice/createShaderModule) will generate a validation error. See the following minimal example and [issue dawn:1510](https://bugs.chromium.org/p/dawn/issues/detail?id=1510).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(!adapter.features.has("shader-f16")){
thrownewError("16-bit floating-point value support is not available");
}
// Explicitly request 16-bit floating-point value support.
constdevice=awaitadapter.requestDevice({
requiredFeatures:["shader-f16"],
});
constcode=`
 enable f16;
 @compute @workgroup_size(1)
 fn main() {
  const c : vec3h = vec3<f16>(1.0h, 2.0h, 3.0h);
 }
`;
constshaderModule=device.createShaderModule({code});
// Create a compute pipeline with this shader module
// and run the shader on the GPU...

```

It's possible to support both `f16` and `f32` types in the WGSL shader module code with an [`alias`](https://gpuweb.github.io/gpuweb/wgsl/#type-aliases) depending on the `"shader-f16"` feature support as shown in the following snippet.
```
constadapter=awaitnavigator.gpu.requestAdapter();
consthasShaderF16=adapter.features.has("shader-f16");
constdevice=awaitadapter.requestDevice({
requiredFeatures:hasShaderF16?["shader-f16"]:[],
});
constheader=hasShaderF16
?`enable f16;
   alias min16float = f16;`
:`alias min16float = f32;`;
constcode=`
${header}
 @compute @workgroup_size(1)
 fn main() {
  const c = vec3<min16float>(1.0, 2.0, 3.0);
 }
`;

```

## Push the limits
The maximum number of bytes necessary to hold one sample (pixel or subpixel) of render pipeline output data, across all color attachments, is 32 bytes by default. It is now possible to request up to 64 by using the [`maxColorAttachmentBytesPerSample`](https://gpuweb.github.io/gpuweb/#dom-supported-limits-maxcolorattachmentbytespersample) limit. See the following example and [issue dawn:2036](https://bugs.chromium.org/p/dawn/issues/detail?id=2036).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(adapter.limits.maxColorAttachmentBytesPerSample64){
// When the desired limit isn't supported, take action to either fall back to
// a code path that does not require the higher limit or notify the user that
// their device does not meet minimum requirements.
}
// Request highest limit of max color attachments bytes per sample.
constdevice=awaitadapter.requestDevice({
requiredLimits:{maxColorAttachmentBytesPerSample:64},
});

```

The [`maxInterStageShaderVariables`](https://gpuweb.github.io/gpuweb/#dom-supported-limits-maxinterstageshadervariables) and [`maxInterStageShaderComponents`](https://gpuweb.github.io/gpuweb/#dom-supported-limits-maxinterstageshadercomponents) limits used for inter-stage communication have been increased on all platforms. See [issue dawn:1448](https://bugs.chromium.org/p/dawn/issues/detail?id=1448) for details.
For each shader stage, the maximum number of bind group layout entries across a pipeline layout which are storage buffers is 8 by default. It is now possible to request up to 10 by using the [`maxStorageBuffersPerShaderStage`](https://gpuweb.github.io/gpuweb/#dom-supported-limits-maxstoragebufferspershaderstage) limit. See [issue dawn:2159](https://bugs.chromium.org/p/dawn/issues/detail?id=2159).
A new [`maxBindGroupsPlusVertexBuffers`](https://gpuweb.github.io/gpuweb/#dom-supported-limits-maxbindgroupsplusvertexbuffers) limit has been added. It consists of the maximum number of bind group and vertex buffer slots used simultaneously, counting any empty slots below the highest index. Its default value is 24. See [issue dawn:1849](https://bugs.chromium.org/p/dawn/issues/detail?id=1849).
## Changes to depth-stencil state
To improve the developer experience, the depth-stencil state [`depthWriteEnabled`](https://gpuweb.github.io/gpuweb/#dom-gpudepthstencilstate-depthwriteenabled) and [`depthCompare`](https://gpuweb.github.io/gpuweb/#dom-gpudepthstencilstate-depthcompare) attributes are not always required anymore: `depthWriteEnabled` is required only for formats with depth, and `depthCompare` is not required for formats with depth if not used at all. See [issue dawn:2132](https://bugs.chromium.org/p/dawn/issues/detail?id=2132).
## Adapter information updates
Non-standard `type` and `backend` adapter info attributes are now available upon calling [requestAdapterInfo()](https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapter/requestAdapterInfo) when the user has enabled the "WebGPU Developer Features" [flag](https://developer.chrome.com/docs/web-platform/chrome-flags#chromeflags) at `chrome://flags/#enable-webgpu-developer-features`. The `type` can be "discrete GPU", "integrated GPU", "CPU", or "unknown". The `backend` is either "WebGPU", "D3D11", "D3D12", "metal", "vulkan", "openGL", "openGLES", or "null". See [issue dawn:2112](https://bugs.chromium.org/p/dawn/issues/detail?id=2112) and [issue dawn:2107](https://bugs.chromium.org/p/dawn/issues/detail?id=2107).
Adapter info backend and type shown on [https://webgpureport.org](https://webgpureport.org/).
The optional `unmaskHints` list parameter in [requestAdapterInfo()](https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapter/requestAdapterInfo) has been removed. See [issue dawn:1427](https://bugs.chromium.org/p/dawn/issues/detail?id=1427).
## Timestamp queries quantization
Timestamp queries allow applications to measure the execution time of GPU commands with nanosecond precision. However, the WebGPU specification makes timestamp queries optional due to [timing attack](https://gpuweb.github.io/gpuweb/#security-timing) concerns. The Chrome team believes that quantizing timestamp queries provides a good compromise between precision and security, by reducing the resolution to 100 microseconds. See [issue dawn:1800](https://bugs.chromium.org/p/dawn/issues/detail?id=1800).
In Chrome, users can disable timestamp quantization by enabling the "WebGPU Developer Features" [flag](https://developer.chrome.com/docs/web-platform/chrome-flags#chromeflags) at `chrome://flags/#enable-webgpu-developer-features`. Note that this flag alone does not enable the [`"timestamp-query"`](https://gpuweb.github.io/gpuweb/#timestamp-query) feature. Its implementation is still experimental and therefore requires the "Unsafe WebGPU Support" flag at `chrome://flags/#enable-unsafe-webgpu`.
In Dawn, a new [device toggle](https://dawn.googlesource.com/dawn.git/+/refs/heads/main/docs/dawn/device_facilities.md#toggles) called "timestamp_quantization" has been added and is enabled by default. The following snippet shows you how to allow the experimental "timestamp-query" feature with no timestamp quantization when requesting a device.
```
wgpu::DawnTogglesDescriptordeviceTogglesDesc={};
constchar*allowUnsafeApisToggle="allow_unsafe_apis";
deviceTogglesDesc.enabledToggles=&allowUnsafeApisToggle;
deviceTogglesDesc.enabledToggleCount=1;
constchar*timestampQuantizationToggle="timestamp_quantization";
deviceTogglesDesc.disabledToggles=&timestampQuantizationToggle;
deviceTogglesDesc.disabledToggleCount=1;
wgpu::DeviceDescriptordesc={.nextInChain=&deviceTogglesDesc};
// Request a device with no timestamp quantization.
myAdapter.RequestDevice(&desc,myCallback,myUserData);

```

## Spring-cleaning features
The experimental "timestamp-query-inside-passes" feature has been renamed to "chromium-experimental-timestamp-query-inside-passes" to make it clear to developers that this feature is experimental and available only in Chromium-based browsers for now. See [issue dawn:1193](https://bugs.chromium.org/p/dawn/issues/detail?id=1193).
The experimental "pipeline-statistics-query" feature, which was only partially implemented, has been removed because it is no longer being developed. See [issue chromium:1177506](https://bugs.chromium.org/p/chromium/issues/detail?id=1177506).
This covers only some of the key highlights. Check out the exhaustive [list of commits](https://dawn.googlesource.com/dawn/+log/chromium/6045..chromium/6099).
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


Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-12-08 UTC.

