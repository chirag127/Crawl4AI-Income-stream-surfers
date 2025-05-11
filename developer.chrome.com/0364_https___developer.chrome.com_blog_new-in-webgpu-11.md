---
url: https://developer.chrome.com/blog/new-in-webgpu-116?hl=en
title: https://developer.chrome.com/blog/new-in-webgpu-116?hl=en
date: 2025-05-11T17:54:13.634872
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-webgpu-116?hl=es-419)




  * On this page
  * [WebCodecs integration](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#webcodecs_integration)
  * [Lost device returned by GPUAdapter requestDevice()](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#lost_device_returned_by_gpuadapter_requestdevice)
  * [Keep video playback smooth if importExternalTexture() is called](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#keep_video_playback_smooth_if_importexternaltexture_is_called)
  * [Spec conformance](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#spec_conformance)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#improving_developer_experience)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#whats-new)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  What's New in WebGPU (Chrome 116) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [WebCodecs integration](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#webcodecs_integration)
  * [Lost device returned by GPUAdapter requestDevice()](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#lost_device_returned_by_gpuadapter_requestdevice)
  * [Keep video playback smooth if importExternalTexture() is called](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#keep_video_playback_smooth_if_importexternaltexture_is_called)
  * [Spec conformance](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#spec_conformance)
  * [Improving developer experience](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#improving_developer_experience)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-116?hl=en#whats-new)


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
## WebCodecs integration
WebGPU exposes an API to create opaque "external texture" objects from `HTMLVideoElement` through [`importExternalTexture()`](https://developer.mozilla.org/docs/Web/API/GPUDevice/importExternalTexture). You can use these objects to sample the video frames efficiently, potentially in a 0-copy way directly from the source [YUV](https://en.wikipedia.org/wiki/YUV) color model data.
However, the initial WebGPU specification did not allow creating `GPUExternalTexture` objects from WebCodecs [`VideoFrame`](https://developer.mozilla.org/docs/Web/API/VideoFrame) objects. This capability is important for advanced video processing apps that already use WebCodecs and would like to integrate WebGPU in the video processing pipeline. WebCodecs integration adds support for using a `VideoFrame` as the source for a [`GPUExternalTexture`](https://developer.mozilla.org/docs/Web/API/GPUExternalTexture) and a [`copyExternalImageToTexture()`](https://developer.mozilla.org/docs/Web/API/GPUQueue/copyExternalImageToTexture) call. See the following example, and the [chromestatus entry](https://chromestatus.com/feature/5078348864159744).
```
// Access the GPU device.
constadapter=awaitnavigator.gpu.requestAdapter();
constdevice=awaitadapter.requestDevice();
// Create VideoFrame from HTMLVideoElement.
constvideo=document.querySelector("video");
constvideoFrame=newVideoFrame(video);
// Create texture from VideoFrame.
consttexture=device.importExternalTexture({source:videoFrame});
// TODO: Use texture in bind group creation.

```

Check out the [Video Uploading with WebCodecs](https://webgpu.github.io/webgpu-samples/samples/videoUploadingWebCodecs) experimental sample to play with it.
## Lost device returned by GPUAdapter requestDevice()
If the [`requestDevice()`](https://developer.mozilla.org/docs/Web/API/GPUAdapter/requestDevice) method on [`GPUAdapter`](https://developer.mozilla.org/docs/Web/API/GPUAdapter) fails because it has been already used to create a [`GPUDevice`](https://developer.mozilla.org/docs/Web/API/GPUDevice), it now fulfills with a `GPUDevice` immediately marked as lost, rather than returning a promise that rejects with `null`. See [issue chromium:1234617](https://bugs.chromium.org/p/chromium/issues/detail?id=1234617).
```
constadapter=awaitnavigator.gpu.requestAdapter();
constdevice1=awaitadapter.requestDevice();
// New! The promise is not rejected anymore with null.
constdevice2=awaitadapter.requestDevice();
// And the device is immediately marked as lost.
constinfo=awaitdevice2.lost;

```

## Keep video playback smooth if importExternalTexture() is called
When [`importExternalTexture()`](https://developer.mozilla.org/docs/Web/API/GPUDevice/importExternalTexture) is called with an `HTMLVideoElement`, the associated video playback is not throttled anymore when the video is not visible in the viewport. See [issue chromium:1425252](https://bugs.chromium.org/p/chromium/issues/detail?id=1425252).
## Spec conformance
The `message` argument in the [`GPUPipelineError()`](https://developer.mozilla.org/docs/Web/API/GPUPipelineError/GPUPipelineError) constructor is optional. See [change chromium:4613967](https://chromium-review.googlesource.com/c/chromium/src/+/4613967).
An error is fired when calling [`createShaderModule()`](https://developer.mozilla.org/docs/Web/API/GPUDevice/createShaderModule) if the WGSL source `code` contains contains `\0`. See [issue dawn:1345](https://bugs.chromium.org/p/dawn/issues/detail?id=1345).
The default maximum level of detail (`lodMaxClamp`) used when sampling a texture with [`createSampler()`](https://developer.mozilla.org/docs/Web/API/GPUDevice/createSampler) is 32. See [change chromium:4608063](https://chromium-review.googlesource.com/c/chromium/src/+/4608063).
## Improving developer experience
A message is displayed in the DevTools JavaScript console to remind developers when they are using WebGPU on an unsupported platform. See [change chromium:4589369](https://chromium-review.googlesource.com/c/chromium/src/+/4589369).
Buffer validation error messages are instantly shown in DevTools JavaScript console when [`getMappedRange()`](https://developer.mozilla.org/docs/Web/API/GPUBuffer/getMappedRange) fails without forcing developers to send commands to the queue. See [change chromium:4597950](https://chromium-review.googlesource.com/c/chromium/src/+/4597950).
Buffer validation error message in DevTools JavaScript console. 
## Dawn updates
The `disallow_unsafe_apis` debug toggle has been renamed to `allow_unsafe_apis` and made its default to disabled. This toggle suppresses validation errors on API entry points or parameter combinations that aren't considered secure yet. It can be useful for [debugging](https://dawn.googlesource.com/dawn/+/refs/heads/main/docs/dawn/debugging.md). See [issue dawn:1685](https://bugs.chromium.org/p/dawn/issues/detail?id=1685).
The `wgpu::ShaderModuleWGSLDescriptor` deprecated `source` attribute is removed in favor of `code`. See [change dawn:130321](https://dawn-review.googlesource.com/c/dawn/+/130321).
The missing `wgpu::RenderBundle::SetLabel()` method has been implemented. See [change dawn:134502](https://dawn-review.googlesource.com/c/dawn/+/134502).
Applications can request a particular backend when getting an adapter with the `wgpu::RequestAdapterOptionsBackendType` option. See an example below and [issue dawn:1875](https://bugs.chromium.org/p/dawn/issues/detail?id=1875).
```
wgpu::RequestAdapterOptionsBackendTypebackendTypeOptions={};
backendTypeOptions.backendType=wgpu::BackendType::D3D12;
wgpu::RequestAdapterOptionsoptions={};
options.nextInChain=&backendTypeOptions;
// Request D3D12 adapter.
myInstance.RequestAdapter(&options,myCallback,myUserData);

```

A new `SwapChain::GetCurrentTexture()` method has been added with additional usages for swapchain textures so that the return `wgpu::Texture` can be used in copies. See an example below and [issue dawn:1551](https://bugs.chromium.org/p/dawn/issues/detail?id=1551).
```
wgpu::SwapChainswapchain=myDevice.CreateSwapChain(mySurface,&myDesc);
swapchain.GetCurrentTexture();
swapchain.Present();

```

This covers only some of the key highlights. Check out the exhaustive [list of commits](https://dawn.googlesource.com/dawn/+log/chromium/5790..chromium/5845).
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
Last updated 2023-08-08 UTC.

