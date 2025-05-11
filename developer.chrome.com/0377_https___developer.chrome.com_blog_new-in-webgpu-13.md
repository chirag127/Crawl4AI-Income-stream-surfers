---
url: https://developer.chrome.com/blog/new-in-webgpu-131?hl=en
title: https://developer.chrome.com/blog/new-in-webgpu-131?hl=en
date: 2025-05-11T17:54:32.046192
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/new-in-webgpu-131?hl=es-419)

Sign in


  * On this page
  * [Clip distances in WGSL](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#clip_distances_in_wgsl)
  * [GPUCanvasContext getConfiguration()](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#gpucanvascontext_getconfiguration)
  * [Point and line primitives must not have depth bias](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#point_and_line_primitives_must_not_have_depth_bias)
  * [Inclusive scan built-in functions for subgroups](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#inclusive_scan_built-in_functions_for_subgroups)
  * [Experimental support for multi-draw indirect](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#experimental_support_for_multi-draw_indirect)
  * [Shader module compilation option strict math](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#shader_module_compilation_option_strict_math)
  * [Remove GPUAdapter requestAdapterInfo()](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#remove_gpuadapter_requestadapterinfo)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#whats-new)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  What's New in WebGPU (Chrome 131) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Clip distances in WGSL](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#clip_distances_in_wgsl)
  * [GPUCanvasContext getConfiguration()](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#gpucanvascontext_getconfiguration)
  * [Point and line primitives must not have depth bias](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#point_and_line_primitives_must_not_have_depth_bias)
  * [Inclusive scan built-in functions for subgroups](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#inclusive_scan_built-in_functions_for_subgroups)
  * [Experimental support for multi-draw indirect](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#experimental_support_for_multi-draw_indirect)
  * [Shader module compilation option strict math](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#shader_module_compilation_option_strict_math)
  * [Remove GPUAdapter requestAdapterInfo()](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#remove_gpuadapter_requestadapterinfo)
  * [What's New in WebGPU](https://developer.chrome.com/blog/new-in-webgpu-131?hl=en#whats-new)


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
## Clip distances in WGSL
Clip distances allow you to restrict [primitives' clip volume](https://gpuweb.github.io/gpuweb/#clip-volume) with user-defined half-spaces in the output of vertex stage. Defining your own clipping planes gives greater control over what's visible in your WebGPU scenes. This technique is particularly useful for applications like CAD software, where precise control over visualization is crucial.
When the `"clip-distances"` feature is available in a GPUAdapter, request a GPUDevice with this feature to get clip distances support in WGSL, and explicitly enable this extension in your WGSL code with `enable clip_distances;`. Once enabled, you can use the `clip_distances` built-in array in your vertex shader. This array holds distances to a user-defined clip plane:
  * A clip distance of 0 means the vertex lies on the plane.
  * A positive distance means the vertex is inside the clip half-space (the side you want to keep).
  * A negative distance means the vertex is outside the clip half-space (the side you want to discard).


See the following snippet, the [chromestatus entry](https://chromestatus.com/feature/5141929256550400), and [issue 358408571](https://issues.chromium.org/issues/358408571).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(!adapter.features.has("clip-distances")){
thrownewError("Clip distances support is not available");
}
// Explicitly request clip distances support.
constdevice=awaitadapter.requestDevice({
requiredFeatures:["clip-distances"],
});
constvertexShaderModule=device.createShaderModule({code:`
 enable clip_distances;
 struct VertexOut {
  @builtin(clip_distances) my_clip_distances : array<f32, 1>,
  @builtin(position) my_position : vec4f,
 }
 @vertex fn main() -> VertexOut {
  var output : VertexOut;
  output.my_clip_distances[0] = 1;
  output.my_position = vec4f(0, 0, 0, 1);
  return output;
 }
`,
});
// Send the appropriate commands to the GPU...

```

## GPUCanvasContext getConfiguration()
Once GPUCanvasContext `configure()` has been called with a configuration dictionary, the GPUCanvasContext [`getConfiguration()`](https://gpuweb.github.io/gpuweb/#dom-gpucanvascontext-getconfiguration) method lets you check the canvas context configuration. It includes `device`, `format`, `usage`, `viewFormats`, `colorSpace`, `toneMapping`, and `alphaMode` members. This is useful for tasks like checking if the browser supports HDR canvas, as shown in the [Particles (HDR) sample](https://webgpu.github.io/webgpu-samples/?sample=particles). See the following snippet, the [chromestatus entry](https://chromestatus.com/feature/6195110870777856), and [issue 370109829](https://issues.chromium.org/issues/370109829).
```
constadapter=awaitnavigator.gpu.requestAdapter();
constdevice=awaitadapter.requestDevice();
constcanvas=document.querySelector("canvas");
constcontext=canvas.getContext("webgpu");
// Configure the canvas for HDR.
context.configure({
device,
format:"rgba16float",
toneMapping:{mode:"extended"},
});
constconfiguration=context.getConfiguration();
if(configuration.toneMapping.mode==="extended"){
// The browser supports HDR canvas.
// Warning! The user still needs a HDR display to enjoy HDR content.
}

```

## Point and line primitives must not have depth bias
As announced [previously](https://developer.chrome.com/blog/new-in-webgpu-128#deprecate_setting_depth_bias_for_lines_and_points), the WebGPU spec now makes it a validation error to set `depthBias`, `depthBiasSlopeScale`, and `depthBiasClamp` to a non-zero value when the topology for a render pipeline is a line or point type. See [issue 352567424](https://issues.chromium.org/issues/352567424).
## Inclusive scan built-in functions for subgroups
As part of the [subgroups experimentation](https://developer.chrome.com/blog/new-in-webgpu-128#experimenting_with_subgroups), the following subgroup built-in functions have been added in [issue 361330160](https://g-issues.chromium.org/issues/361330160):
  * `subgroupInclusiveAdd(value)`: Returns the inclusive scan summation of all active invocations `value`s across the subgroup.
  * `subgroupInclusiveMul(value)`: Returns the inclusive scan multiplication of all active invocations `value`s across the subgroup.


## Experimental support for multi-draw indirect
The multi-draw indirect GPU feature lets you issue multiple draw calls with a single GPU command. This is particularly useful in situations where a large number of objects need to be rendered, such as particle systems, instancing, and large scenes. The `drawIndirect()` and `drawIndexedIndirect()` GPURenderPassEncoder methods can only issue a single draw call at a time from a certain region of a GPU buffer.
Until this experimental feature is [standardized](https://github.com/gpuweb/gpuweb/pull/2315), enable the "Unsafe WebGPU Support" flag at `chrome://flags/#enable-unsafe-webgpu` to make it available in Chrome.
With the `"chromium-experimental-multi-draw-indirect"` non-standard GPU feature available in a GPUAdapter, request a GPUDevice with this feature. Then create a GPUBuffer with the `GPUBufferUsage.INDIRECT` usage to store the draw calls. You can use it later in the new `multiDrawIndirect()` and `multiDrawIndexedIndirect()` GPURenderPassEncoder methods to issue draw calls inside a render pass. See the following snippet and [issue 356461286](https://issues.chromium.org/issues/356461286).
```
constadapter=awaitnavigator.gpu.requestAdapter();
if(!adapter.features.has("chromium-experimental-multi-draw-indirect")){
thrownewError("Experimental multi-draw indirect support is not available");
}
// Explicitly request experimental multi-draw indirect support.
constdevice=awaitadapter.requestDevice({
requiredFeatures:["chromium-experimental-multi-draw-indirect"],
});
// Draw call have vertexCount, instanceCount, firstVertex, and firstInstance parameters.
constdrawData=newUint32Array([
3,1,0,0,// First draw call
3,1,3,0,// Second draw call
]);
// Create a buffer to store the draw calls.
constdrawBuffer=device.createBuffer({
size:drawData.byteLength,
usage:GPUBufferUsage.INDIRECT|GPUBufferUsage.COPY_DST,
});
device.queue.writeBuffer(drawBuffer,0,drawData);
// Create a render pipeline, a vertex buffer, and a render pass encoder...
// Inside a render pass, issue the draw calls.
myPassEncoder.setPipeline(myPipeline);
myPassEncoder.setVertexBuffer(0,myVertexBuffer);
myPassEncoder.multiDrawIndirect(drawBuffer,/*offset=*/0,/*maxDrawCount=*/2);
myPassEncoder.end();

```

## Shader module compilation option strict math
A boolean `strictMath` developer option has been added to GPUShaderModuleDescriptor to let you enable or disable strict math during shader module compilation. It is available behind the "WebGPU Developer Features" flag at `chrome://flags/#enable-webgpu-developer-features`, which means it is a feature intended only for use during development. See [issue 42241455](https://issues.chromium.org/issues/42241455).
This option is currently supported on Metal and Direct3D. When strict math is disabled, the compiler may optimize your shaders by:
  * Ignoring the possibility of NaN and Infinity values.
  * Treating -0 as +0.
  * Replacing division with faster multiplication by the reciprocal.
  * Rearranging operations based on associative and distributive properties.

```
constadapter=awaitnavigator.gpu.requestAdapter();
constdevice=awaitadapter.requestDevice();
constcode=`
 // Examines the bit pattern of the floating-point number to
 // determine if it represents a NaN according to the IEEE 754 standard.
 fn isNan(x : f32) -> bool {
  bool ones_exp = (bitcast<u32>(x) & 0x7f8) == 0x7f8;
  bool non_zero_sig = (bitcast<u32>(x) & 0x7ffff) != 0;
  return ones_exp && non_zero_sig;
 }
 // ...
`;
// Enable strict math during shader compilation.
constshaderModule=device.createShaderModule({code,strictMath:true});

```

## Remove GPUAdapter requestAdapterInfo()
The GPUAdapter `requestAdapterInfo()` asynchronous method is redundant as you can already get GPUAdapterInfo synchronously using the GPUAdapter `info` attribute. Hence, the non-standard GPUAdapter `requestAdapterInfo()` method is now removed. See the [intent to remove](https://groups.google.com/a/chromium.org/g/blink-dev/c/HxOgGf4NzQ4).
## Dawn updates
The `tint_benchmark` executable measures the cost of translating shaders from WGSL to each backend language. Check out the new [documentation](https://dawn.googlesource.com/dawn/+/main/docs/tint/benchmark.md) to learn more about it.
This covers only some of the key highlights. Check out the exhaustive [list of commits](https://dawn.googlesource.com/dawn/+log/chromium/6723..chromium/6778?n=1000).
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
Last updated 2024-11-06 UTC.

