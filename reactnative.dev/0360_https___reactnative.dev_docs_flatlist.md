---
url: https://reactnative.dev/docs/flatlist
title: https://reactnative.dev/docs/flatlist
date: 2025-05-10T21:40:05.296759
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/flatlist#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
A performant interface for rendering basic, flat lists, supporting the most handy features:
  * Fully cross-platform.
  * Optional horizontal mode.
  * Configurable viewability callbacks.
  * Header support.
  * Footer support.
  * Separator support.
  * Pull to Refresh.
  * Scroll loading.
  * ScrollToIndex support.
  * Multiple column support.


If you need section support, use [`<SectionList>`](https://reactnative.dev/docs/sectionlist).
## Example[​](https://reactnative.dev/docs/flatlist#example "Direct link to Example")
  * TypeScript
  * JavaScript


To render multiple columns, use the [`numColumns`](https://reactnative.dev/docs/flatlist#numcolumns) prop. Using this approach instead of a `flexWrap` layout can prevent conflicts with the item height logic.
More complex, selectable example below.
  * By passing `extraData={selectedId}` to `FlatList` we make sure `FlatList` itself will re-render when the state changes. Without setting this prop, `FlatList` would not know it needs to re-render any items because it is a `PureComponent` and the prop comparison will not show any changes.
  * `keyExtractor` tells the list to use the `id`s for the react keys instead of the default `key` property.


  * TypeScript
  * JavaScript


This is a convenience wrapper around [`<VirtualizedList>`](https://reactnative.dev/docs/virtualizedlist), and thus inherits its props (as well as those of [`<ScrollView>`](https://reactnative.dev/docs/scrollview)) that aren't explicitly listed here, along with the following caveats:
  * Internal state is not preserved when content scrolls out of the render window. Make sure all your data is captured in the item data or external stores like Flux, Redux, or Relay.
  * This is a `PureComponent` which means that it will not re-render if `props` remain shallow-equal. Make sure that everything your `renderItem` function depends on is passed as a prop (e.g. `extraData`) that is not `===` after updates, otherwise your UI may not update on changes. This includes the `data` prop and parent component state.
  * In order to constrain memory and enable smooth scrolling, content is rendered asynchronously offscreen. This means it's possible to scroll faster than the fill rate and momentarily see blank content. This is a tradeoff that can be adjusted to suit the needs of each application, and we are working on improving it behind the scenes.
  * By default, the list looks for a `key` prop on each item and uses that for the React key. Alternatively, you can provide a custom `keyExtractor` prop.


# Reference
## Props[​](https://reactnative.dev/docs/flatlist#props "Direct link to Props")
### [VirtualizedList Props](https://reactnative.dev/docs/virtualizedlist#props)[​](https://reactnative.dev/docs/flatlist#virtualizedlist-props "Direct link to virtualizedlist-props")
Inherits [VirtualizedList Props](https://reactnative.dev/docs/virtualizedlist#props).
### 
Required
**`renderItem`**[​](https://reactnative.dev/docs/flatlist#required-renderitem "Direct link to required-renderitem")
tsx
```
renderItem({ item:ItemT, index:number, separators:{highlight:()=>void;unhighlight:()=>void;  updateProps:(select:'leading'|'trailing', newProps:any)=>void;}):JSX.Element;
```

Takes an item from `data` and renders it into the list.
Provides additional metadata like `index` if you need it, as well as a more generic `separators.updateProps` function which let you set whatever props you want to change the rendering of either the leading separator or trailing separator in case the more common `highlight` and `unhighlight` (which set the `highlighted: boolean` prop) are insufficient for your use case.
Type  
---  
function  
  * `item` (Object): The item from `data` being rendered.
  * `index` (number): The index corresponding to this item in the `data` array.
  * `separators` (Object) 
    * `highlight` (Function)
    * `unhighlight` (Function)
    * `updateProps` (Function) 
      * `select` (enum('leading', 'trailing'))
      * `newProps` (Object)


Example usage:
tsx
```
<FlatListItemSeparatorComponent={Platform.OS!=='android'&&(({highlighted})=>(<Viewstyle={[style.separator, highlighted &&{marginLeft:0}]}/>data={[{title:'Title Text', key:'item1'}]}renderItem={({item, index, separators})=>(<TouchableHighlightkey={item.key}onPress={()=>this._onPress(item)}onShowUnderlay={separators.highlight}onHideUnderlay={separators.unhighlight}><Viewstyle={{backgroundColor:'white'}}><Text>{item.title}</Text></View></TouchableHighlight>/>
```

### 
Required
**`data`**[​](https://reactnative.dev/docs/flatlist#required-data "Direct link to required-data")
An array (or array-like list) of items to render. Other data types can be used by targeting [`VirtualizedList`](https://reactnative.dev/docs/virtualizedlist) directly.
Type  
---  
ArrayLike  
### `ItemSeparatorComponent`[​](https://reactnative.dev/docs/flatlist#itemseparatorcomponent "Direct link to itemseparatorcomponent")
Rendered in between each item, but not at the top or bottom. By default, `highlighted` and `leadingItem` props are provided. `renderItem` provides `separators.highlight`/`unhighlight` which will update the `highlighted` prop, but you can also add custom props with `separators.updateProps`. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, function, element  
### `ListEmptyComponent`[​](https://reactnative.dev/docs/flatlist#listemptycomponent "Direct link to listemptycomponent")
Rendered when the list is empty. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListFooterComponent`[​](https://reactnative.dev/docs/flatlist#listfootercomponent "Direct link to listfootercomponent")
Rendered at the bottom of all the items. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListFooterComponentStyle`[​](https://reactnative.dev/docs/flatlist#listfootercomponentstyle "Direct link to listfootercomponentstyle")
Styling for internal View for `ListFooterComponent`.
Type  
---  
### `ListHeaderComponent`[​](https://reactnative.dev/docs/flatlist#listheadercomponent "Direct link to listheadercomponent")
Rendered at the top of all the items. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListHeaderComponentStyle`[​](https://reactnative.dev/docs/flatlist#listheadercomponentstyle "Direct link to listheadercomponentstyle")
Styling for internal View for `ListHeaderComponent`.
Type  
---  
### `columnWrapperStyle`[​](https://reactnative.dev/docs/flatlist#columnwrapperstyle "Direct link to columnwrapperstyle")
Optional custom style for multi-item rows generated when `numColumns > 1`.
Type  
---  
### `extraData`[​](https://reactnative.dev/docs/flatlist#extradata "Direct link to extradata")
A marker property for telling the list to re-render (since it implements `PureComponent`). If any of your `renderItem`, Header, Footer, etc. functions depend on anything outside of the `data` prop, stick it here and treat it immutably.
Type  
---  
any  
### `getItemLayout`[​](https://reactnative.dev/docs/flatlist#getitemlayout "Direct link to getitemlayout")
tsx
```
(data, index)=>{length:number, offset:number, index:number}
```

`getItemLayout` is an optional optimization that allows skipping the measurement of dynamic content if you know the size (height or width) of items ahead of time. `getItemLayout` is efficient if you have fixed size items, for example:
tsx
```
 getItemLayout={(data, index)=>({length:ITEM_HEIGHT, offset:ITEM_HEIGHT* index, index}
```

Adding `getItemLayout` can be a great performance boost for lists of several hundred items. Remember to include separator length (height or width) in your offset calculation if you specify `ItemSeparatorComponent`.
Type  
---  
function  
### `horizontal`[​](https://reactnative.dev/docs/flatlist#horizontal "Direct link to horizontal")
If `true`, renders items next to each other horizontally instead of stacked vertically.
Type  
---  
boolean  
### `initialNumToRender`[​](https://reactnative.dev/docs/flatlist#initialnumtorender "Direct link to initialnumtorender")
How many items to render in the initial batch. This should be enough to fill the screen but not much more. Note these items will never be unmounted as part of the windowed rendering in order to improve perceived performance of scroll-to-top actions.
Type| Default  
---|---  
number| `10`  
### `initialScrollIndex`[​](https://reactnative.dev/docs/flatlist#initialscrollindex "Direct link to initialscrollindex")
Instead of starting at the top with the first item, start at `initialScrollIndex`. This disables the "scroll to top" optimization that keeps the first `initialNumToRender` items always rendered and immediately renders the items starting at this initial index. Requires `getItemLayout` to be implemented.
Type  
---  
number  
### `inverted`[​](https://reactnative.dev/docs/flatlist#inverted "Direct link to inverted")
Reverses the direction of scroll. Uses scale transforms of `-1`.
Type  
---  
boolean  
### `keyExtractor`[​](https://reactnative.dev/docs/flatlist#keyextractor "Direct link to keyextractor")
tsx
```
(item:ItemT, index:number)=>string;
```

Used to extract a unique key for a given item at the specified index. Key is used for caching and as the react key to track item re-ordering. The default extractor checks `item.key`, then `item.id`, and then falls back to using the index, like React does.
Type  
---  
function  
### `numColumns`[​](https://reactnative.dev/docs/flatlist#numcolumns "Direct link to numcolumns")
Multiple columns can only be rendered with `horizontal={false}` and will zig-zag like a `flexWrap` layout. Items should all be the same height - masonry layouts are not supported.
Type  
---  
number  
### `onRefresh`[​](https://reactnative.dev/docs/flatlist#onrefresh "Direct link to onrefresh")
tsx
```
()=>void;
```

If provided, a standard RefreshControl will be added for "Pull to Refresh" functionality. Make sure to also set the `refreshing` prop correctly.
Type  
---  
function  
### `onViewableItemsChanged`[​](https://reactnative.dev/docs/flatlist#onviewableitemschanged "Direct link to onviewableitemschanged")
Called when the viewability of rows changes, as defined by the `viewabilityConfig` prop.
Type  
---  
`(callback: {changed: ViewToken[](https://reactnative.dev/docs/viewtoken)[], viewableItems: ViewToken[](https://reactnative.dev/docs/viewtoken)[]} => void;`  
### `progressViewOffset`[​](https://reactnative.dev/docs/flatlist#progressviewoffset "Direct link to progressviewoffset")
Set this when offset is needed for the loading indicator to show correctly.
Type  
---  
number  
### `refreshing`[​](https://reactnative.dev/docs/flatlist#refreshing "Direct link to refreshing")
Set this true while waiting for new data from a refresh.
Type  
---  
boolean  
### `removeClippedSubviews`[​](https://reactnative.dev/docs/flatlist#removeclippedsubviews "Direct link to removeclippedsubviews")
This may improve scroll performance for large lists. On Android the default value is `true`.
> Note: May have bugs (missing content) in some circumstances - use at your own risk.
Type  
---  
boolean  
### `viewabilityConfig`[​](https://reactnative.dev/docs/flatlist#viewabilityconfig "Direct link to viewabilityconfig")
See [`ViewabilityHelper.js`](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js) for flow type and further documentation.
Type  
---  
ViewabilityConfig  
`viewabilityConfig` takes a type `ViewabilityConfig` an object with following properties
Property| Type  
---|---  
minimumViewTime| number  
viewAreaCoveragePercentThreshold| number  
itemVisiblePercentThreshold| number  
waitForInteraction| boolean  
At least one of the `viewAreaCoveragePercentThreshold` or `itemVisiblePercentThreshold` is required. This needs to be done in the `constructor` to avoid following error ([ref](https://github.com/facebook/react-native/issues/17408)):
```
Error:Changing viewabilityConfig on the fly is not supported
```

tsx
```
constructor(props){super(props)this.viewabilityConfig={   waitForInteraction:true,   viewAreaCoveragePercentThreshold:95
```

tsx
```
<FlatList  viewabilityConfig={this.viewabilityConfig}...
```

#### minimumViewTime[​](https://reactnative.dev/docs/flatlist#minimumviewtime "Direct link to minimumViewTime")
Minimum amount of time (in milliseconds) that an item must be physically viewable before the viewability callback will be fired. A high number means that scrolling through content without stopping will not mark the content as viewable.
#### viewAreaCoveragePercentThreshold[​](https://reactnative.dev/docs/flatlist#viewareacoveragepercentthreshold "Direct link to viewAreaCoveragePercentThreshold")
Percent of viewport that must be covered for a partially occluded item to count as "viewable", 0-100. Fully visible items are always considered viewable. A value of 0 means that a single pixel in the viewport makes the item viewable, and a value of 100 means that an item must be either entirely visible or cover the entire viewport to count as viewable.
#### itemVisiblePercentThreshold[​](https://reactnative.dev/docs/flatlist#itemvisiblepercentthreshold "Direct link to itemVisiblePercentThreshold")
Similar to `viewAreaCoveragePercentThreshold`, but considers the percent of the item that is visible, rather than the fraction of the viewable area it covers.
#### waitForInteraction[​](https://reactnative.dev/docs/flatlist#waitforinteraction "Direct link to waitForInteraction")
Nothing is considered viewable until the user scrolls or `recordInteraction` is called after render.
### `viewabilityConfigCallbackPairs`[​](https://reactnative.dev/docs/flatlist#viewabilityconfigcallbackpairs "Direct link to viewabilityconfigcallbackpairs")
List of `ViewabilityConfig`/`onViewableItemsChanged` pairs. A specific `onViewableItemsChanged` will be called when its corresponding `ViewabilityConfig`'s conditions are met. See `ViewabilityHelper.js` for flow type and further documentation.
Type  
---  
array of ViewabilityConfigCallbackPair  
## Methods[​](https://reactnative.dev/docs/flatlist#methods "Direct link to Methods")
### `flashScrollIndicators()`[​](https://reactnative.dev/docs/flatlist#flashscrollindicators "Direct link to flashscrollindicators")
tsx
```
flashScrollIndicators();
```

Displays the scroll indicators momentarily.
### `getNativeScrollRef()`[​](https://reactnative.dev/docs/flatlist#getnativescrollref "Direct link to getnativescrollref")
tsx
```
getNativeScrollRef():React.ElementRef<typeofScrollViewComponent>;
```

Provides a reference to the underlying scroll component
### `getScrollResponder()`[​](https://reactnative.dev/docs/flatlist#getscrollresponder "Direct link to getscrollresponder")
tsx
```
getScrollResponder():ScrollResponderMixin;
```

Provides a handle to the underlying scroll responder.
### `getScrollableNode()`[​](https://reactnative.dev/docs/flatlist#getscrollablenode "Direct link to getscrollablenode")
tsx
```
getScrollableNode():any;
```

Provides a handle to the underlying scroll node.
### `scrollToEnd()`[​](https://reactnative.dev/docs/flatlist#scrolltoend "Direct link to scrolltoend")
tsx
```
scrollToEnd(params?:{animated?:boolean});
```

Scrolls to the end of the content. May be janky without `getItemLayout` prop.
**Parameters:**
Name| Type  
---|---  
params| object  
Valid `params` keys are:
  * 'animated' (boolean) - Whether the list should do an animation while scrolling. Defaults to `true`.


### `scrollToIndex()`[​](https://reactnative.dev/docs/flatlist#scrolltoindex "Direct link to scrolltoindex")
tsx
```
scrollToIndex:(params:{ index:number; animated?:boolean; viewOffset?:number; viewPosition?:number;});
```

Scrolls to the item at the specified index such that it is positioned in the viewable area such that `viewPosition` 0 places it at the top, 1 at the bottom, and 0.5 centered in the middle.
> Note: Cannot scroll to locations outside the render window without specifying the `getItemLayout` prop.
**Parameters:**
Name| Type  
---|---  
params Required| object  
Valid `params` keys are:
  * 'animated' (boolean) - Whether the list should do an animation while scrolling. Defaults to `true`.
  * 'index' (number) - The index to scroll to. Required.
  * 'viewOffset' (number) - A fixed number of pixels to offset the final target position.
  * 'viewPosition' (number) - A value of `0` places the item specified by index at the top, `1` at the bottom, and `0.5` centered in the middle.


### `scrollToItem()`[​](https://reactnative.dev/docs/flatlist#scrolltoitem "Direct link to scrolltoitem")
tsx
```
scrollToItem(params:{ animated?:?boolean, item:Item, viewPosition?:number,});
```

Requires linear scan through data - use `scrollToIndex` instead if possible.
> Note: Cannot scroll to locations outside the render window without specifying the `getItemLayout` prop.
**Parameters:**
Name| Type  
---|---  
params Required| object  
Valid `params` keys are:
  * 'animated' (boolean) - Whether the list should do an animation while scrolling. Defaults to `true`.
  * 'item' (object) - The item to scroll to. Required.
  * 'viewPosition' (number)


### `scrollToOffset()`[​](https://reactnative.dev/docs/flatlist#scrolltooffset "Direct link to scrolltooffset")
tsx
```
scrollToOffset(params:{ offset:number; animated?:boolean;});
```

Scroll to a specific content pixel offset in the list.
**Parameters:**
Name| Type  
---|---  
params Required| object  
Valid `params` keys are:
  * 'offset' (number) - The offset to scroll to. In case of `horizontal` being true, the offset is the x-value, in any other case the offset is the y-value. Required.
  * 'animated' (boolean) - Whether the list should do an animation while scrolling. Defaults to `true`.


Is this page useful?
  * [Props](https://reactnative.dev/docs/flatlist#props)
    * [VirtualizedList Props](https://reactnative.dev/docs/flatlist#virtualizedlist-props)
    * [Required **`renderItem`**](https://reactnative.dev/docs/flatlist#required-renderitem)
    * [Required **`data`**](https://reactnative.dev/docs/flatlist#required-data)
    * [`ItemSeparatorComponent`](https://reactnative.dev/docs/flatlist#itemseparatorcomponent)
    * [`ListEmptyComponent`](https://reactnative.dev/docs/flatlist#listemptycomponent)
    * [`ListFooterComponent`](https://reactnative.dev/docs/flatlist#listfootercomponent)
    * [`ListFooterComponentStyle`](https://reactnative.dev/docs/flatlist#listfootercomponentstyle)
    * [`ListHeaderComponent`](https://reactnative.dev/docs/flatlist#listheadercomponent)
    * [`ListHeaderComponentStyle`](https://reactnative.dev/docs/flatlist#listheadercomponentstyle)
    * [`columnWrapperStyle`](https://reactnative.dev/docs/flatlist#columnwrapperstyle)
    * [`initialNumToRender`](https://reactnative.dev/docs/flatlist#initialnumtorender)
    * [`initialScrollIndex`](https://reactnative.dev/docs/flatlist#initialscrollindex)
    * [`onViewableItemsChanged`](https://reactnative.dev/docs/flatlist#onviewableitemschanged)
    * [`progressViewOffset`](https://reactnative.dev/docs/flatlist#progressviewoffset)
    * [`removeClippedSubviews`](https://reactnative.dev/docs/flatlist#removeclippedsubviews)
    * [`viewabilityConfig`](https://reactnative.dev/docs/flatlist#viewabilityconfig)
    * [`viewabilityConfigCallbackPairs`](https://reactnative.dev/docs/flatlist#viewabilityconfigcallbackpairs)
  * [Methods](https://reactnative.dev/docs/flatlist#methods)
    * [`flashScrollIndicators()`](https://reactnative.dev/docs/flatlist#flashscrollindicators)
    * [`getNativeScrollRef()`](https://reactnative.dev/docs/flatlist#getnativescrollref)
    * [`getScrollResponder()`](https://reactnative.dev/docs/flatlist#getscrollresponder)
    * [`getScrollableNode()`](https://reactnative.dev/docs/flatlist#getscrollablenode)
    * [`scrollToIndex()`](https://reactnative.dev/docs/flatlist#scrolltoindex)
    * [`scrollToOffset()`](https://reactnative.dev/docs/flatlist#scrolltooffset)



