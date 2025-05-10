---
url: https://reactnative.dev/docs/easing
title: https://reactnative.dev/docs/easing
date: 2025-05-10T21:40:05.305300
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/easing#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
The `Easing` module implements common easing functions. This module is used by [`Animated.timing()`](https://reactnative.dev/docs/animated#timing) to convey physically believable motion in animations.
You can find a visualization of some common easing functions at <https://easings.net/>
### Predefined animations[​](https://reactnative.dev/docs/easing#predefined-animations "Direct link to Predefined animations")
The `Easing` module provides several predefined animations through the following methods:
  * [`back`](https://reactnative.dev/docs/easing#back) provides a basic animation where the object goes slightly back before moving forward
  * [`bounce`](https://reactnative.dev/docs/easing#bounce) provides a bouncing animation
  * [`ease`](https://reactnative.dev/docs/easing#ease) provides a basic inertial animation
  * [`elastic`](https://reactnative.dev/docs/easing#elastic) provides a basic spring interaction


### Standard functions[​](https://reactnative.dev/docs/easing#standard-functions "Direct link to Standard functions")
Three standard easing functions are provided:


The [`poly`](https://reactnative.dev/docs/easing#poly) function can be used to implement quartic, quintic, and other higher power functions.
### Additional functions[​](https://reactnative.dev/docs/easing#additional-functions "Direct link to Additional functions")
Additional mathematical functions are provided by the following methods:
  * [`bezier`](https://reactnative.dev/docs/easing#bezier) provides a cubic bezier curve
  * [`circle`](https://reactnative.dev/docs/easing#circle) provides a circular function
  * [`sin`](https://reactnative.dev/docs/easing#sin) provides a sinusoidal function
  * [`exp`](https://reactnative.dev/docs/easing#exp) provides an exponential function


The following helpers are used to modify other easing functions.
  * [`in`](https://reactnative.dev/docs/easing#in) runs an easing function forwards
  * [`inOut`](https://reactnative.dev/docs/easing#inout) makes any easing function symmetrical
  * [`out`](https://reactnative.dev/docs/easing#out) runs an easing function backwards


## Example[​](https://reactnative.dev/docs/easing#example "Direct link to Example")
  * TypeScript
  * JavaScript


# Reference
## Methods[​](https://reactnative.dev/docs/easing#methods "Direct link to Methods")
### `step0()`[​](https://reactnative.dev/docs/easing#step0 "Direct link to step0")
tsx
```
staticstep0(n:number);
```

A stepping function, returns 1 for any positive value of `n`.
### `step1()`[​](https://reactnative.dev/docs/easing#step1 "Direct link to step1")
tsx
```
staticstep1(n:number);
```

A stepping function, returns 1 if `n` is greater than or equal to 1.
### `linear()`[​](https://reactnative.dev/docs/easing#linear "Direct link to linear")
tsx
```
staticlinear(t:number);
```

A linear function, `f(t) = t`. Position correlates to elapsed time one to one.
<https://cubic-bezier.com/#0,0,1,1>
### `ease()`[​](https://reactnative.dev/docs/easing#ease "Direct link to ease")
tsx
```
staticease(t:number);
```

A basic inertial interaction, similar to an object slowly accelerating to speed.
<https://cubic-bezier.com/#.42,0,1,1>
### `quad()`[​](https://reactnative.dev/docs/easing#quad "Direct link to quad")
tsx
```
staticquad(t:number);
```

A quadratic function, `f(t) = t * t`. Position equals the square of elapsed time.
<https://easings.net/#easeInQuad>
### `cubic()`[​](https://reactnative.dev/docs/easing#cubic "Direct link to cubic")
tsx
```
staticcubic(t:number);
```

A cubic function, `f(t) = t * t * t`. Position equals the cube of elapsed time.
<https://easings.net/#easeInCubic>
### `poly()`[​](https://reactnative.dev/docs/easing#poly "Direct link to poly")
tsx
```
staticpoly(n:number);
```

A power function. Position is equal to the Nth power of elapsed time.
n = 4: <https://easings.net/#easeInQuart> n = 5: <https://easings.net/#easeInQuint>
### `sin()`[​](https://reactnative.dev/docs/easing#sin "Direct link to sin")
tsx
```
staticsin(t:number);
```

A sinusoidal function.
<https://easings.net/#easeInSine>
### `circle()`[​](https://reactnative.dev/docs/easing#circle "Direct link to circle")
tsx
```
staticcircle(t:number);
```

A circular function.
<https://easings.net/#easeInCirc>
### `exp()`[​](https://reactnative.dev/docs/easing#exp "Direct link to exp")
tsx
```
staticexp(t:number);
```

An exponential function.
<https://easings.net/#easeInExpo>
### `elastic()`[​](https://reactnative.dev/docs/easing#elastic "Direct link to elastic")
tsx
```
staticelastic(bounciness:number);
```

A basic elastic interaction, similar to a spring oscillating back and forth.
Default bounciness is 1, which overshoots a little bit once. 0 bounciness doesn't overshoot at all, and bounciness of N > 1 will overshoot about N times.
<https://easings.net/#easeInElastic>
### `back()`[​](https://reactnative.dev/docs/easing#back "Direct link to back")
tsx
```
staticback(s)
```

Use with `Animated.parallel()` to create a basic effect where the object animates back slightly as the animation starts.
### `bounce()`[​](https://reactnative.dev/docs/easing#bounce "Direct link to bounce")
tsx
```
staticbounce(t:number);
```

Provides a basic bouncing effect.
<https://easings.net/#easeInBounce>
### `bezier()`[​](https://reactnative.dev/docs/easing#bezier "Direct link to bezier")
tsx
```
staticbezier(x1:number, y1:number, x2:number, y2:number);
```

Provides a cubic bezier curve, equivalent to CSS Transitions' `transition-timing-function`.
A useful tool to visualize cubic bezier curves can be found at <https://cubic-bezier.com/>
### `in()`[​](https://reactnative.dev/docs/easing#in "Direct link to in")
tsx
```
staticin(easing:number);
```

Runs an easing function forwards.
### `out()`[​](https://reactnative.dev/docs/easing#out "Direct link to out")
tsx
```
staticout(easing:number);
```

Runs an easing function backwards.
### `inOut()`[​](https://reactnative.dev/docs/easing#inout "Direct link to inout")
tsx
```
staticinOut(easing:number);
```

Makes any easing function symmetrical. The easing function will run forwards for half of the duration, then backwards for the rest of the duration.
Is this page useful?
  * [Predefined animations](https://reactnative.dev/docs/easing#predefined-animations)
  * [Standard functions](https://reactnative.dev/docs/easing#standard-functions)
  * [Additional functions](https://reactnative.dev/docs/easing#additional-functions)
  * [Methods](https://reactnative.dev/docs/easing#methods)



