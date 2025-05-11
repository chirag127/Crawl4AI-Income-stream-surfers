---
url: https://developer.chrome.com/blog/crux-2025-02?hl=en
title: https://developer.chrome.com/blog/crux-2025-02?hl=en
date: 2025-05-11T16:54:35.803123
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/crux-2025-02?hl=en#main-content)
Sign in


  * On this page
  * [LCP diagnostic information](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_diagnostic_information)
    * [LCP image subparts](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_image_subparts)
    * [LCP resource types](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_resource_types)
  * [RTT diagnostic information](https://developer.chrome.com/blog/crux-2025-02?hl=en#rtt_diagnostic_information)
  * [Removal of the ECT dimension](https://developer.chrome.com/blog/crux-2025-02?hl=en#removal_of_the_ect_dimension)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  LCP image subparts and RTT now available in CrUX 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [LCP diagnostic information](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_diagnostic_information)
    * [LCP image subparts](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_image_subparts)
    * [LCP resource types](https://developer.chrome.com/blog/crux-2025-02?hl=en#lcp_resource_types)
  * [RTT diagnostic information](https://developer.chrome.com/blog/crux-2025-02?hl=en#rtt_diagnostic_information)
  * [Removal of the ECT dimension](https://developer.chrome.com/blog/crux-2025-02?hl=en#removal_of_the_ect_dimension)


Barry Pollard 
[ GitHub ](https://github.com/tunetheweb) [ Mastodon ](https://webperf.social/@tunetheweb) [ Bluesky ](https://bsky.app/profile/tunetheweb.com) [ Homepage ](https://www.tunetheweb.com)
Johannes Henkel 
[ GitHub ](https://github.com/powdercloud) [ Mastodon ](https://mastodon.social/@powdercloud)
Published: February 11, 2025 
The February 2025 release of the [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux) includes a number of exciting new (and changed!) metrics:
  * [Largest Contentful Paint (LCP)](https://web.dev/articles/lcp) image subparts and resource types
  * Round Trip Time (RTT) details
  * Removal of the Effective Connection Type (ECT) dimension


Each of these provide greater insight into the performance metrics of origins and URLs available in CrUX and in this post we'll detail why.
## LCP diagnostic information
We originally introduced [the concept of LCP subparts in Google I/O 2022](https://www.youtube.com/watch?v=fWoI9DXmpdk) as an effective technique to break down LCP time for pages with image LCPs into smaller components to ensure you were spending your efforts optimizing the correct cause(s) of high LCP.
Analysis of HTTP Archive lab data in that talk showed that image download time was often the smallest part of LCP time. A lot of lab tools (including Google's own Lighthouse) frequently concentrated on advice to optimize image formats and size to reduce download times and improve performance. While still correct, the analysis showed that the advice may have been overemphasised and a bigger problem was in delays before the image was found by the browser and started to be downloaded.
While analysing lab data can be useful, how the web is used in real life can often differ so being able to see these subparts for field data is critical. A post published last year confirmed that [common misconception about how to optimize LCP](https://web.dev/blog/common-misconceptions-lcp) with field data.
### LCP image subparts
With this release, site owners may check their own sites for the subparts for image LCP, at the origin or the URL level.
Subparts are only available for images and this does not include first video frame images (which are a little more complicated as we cannot measure the full download time). Text subparts are also not included since they are less useful and would distort image LCPs numbers. For sites that are largely made of text LCPs the overall TTFB and overall FCP metrics are useful breakdowns—though note they are across all LCPs and not specific to text LCPs. Finally, image subparts are only collected on full page loads—unlike the LCP metric itself which is also collected on back-forward navigations and prerendered pages.
This data has been added to [the CrUX API](https://developer.chrome.com/docs/crux/api) and the [CrUX History API](https://developer.chrome.com/docs/crux/history-api) from February 2025 (note: not BigQuery). The CrUX History API has two weeks of data at launch, and this will grow over time to the full 25-week history. The APIs make the data available as the 75th percentile of each subpart expressed in milliseconds.
For example, to get the LCP image subparts for `https://web.dev/` for `PHONE` pageviews you can use the following curl command (replacing `API_KEY` with [your own key](https://developer.chrome.com/docs/crux/api#crux_api_key)):
```
curl"https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=API_KEY"\
--header'Content-Type: application/json'\
--data'{ "formFactor": "PHONE",
      "url": "https://web.dev/",
      "metrics": [
       "largest_contentful_paint_image_time_to_first_byte",
       "largest_contentful_paint_image_resource_load_delay",
       "largest_contentful_paint_image_resource_load_duration",
       "largest_contentful_paint_image_element_render_delay"]}'

```

And you'll get something like this back:
```
{
"record":{
"key":{
"formFactor":"PHONE",
"url":"https://web.dev/"
},
"metrics":{
"largest_contentful_paint_image_element_render_delay":{
"percentiles":{
"p75":2088
}
},
"largest_contentful_paint_image_resource_load_delay":{
"percentiles":{
"p75":828
}
},
"largest_contentful_paint_image_resource_load_duration":{
"percentiles":{
"p75":417
}
},
"largest_contentful_paint_image_time_to_first_byte":{
"percentiles":{
"p75":2385
}
}
},
"collectionPeriod":{
"firstDate":{
"year":2025,
"month":1,
"day":12
},
"lastDate":{
"year":2025,
"month":2,
"day":8
}
}
}
}

```

We have updated the [CrUX Vis tool](https://cruxvis.withgoogle.com/#/) to include this data and expect other third-party tools that use the CrUX APIs to also expose this valuable data:
LCP image subparts in CrUX Vis.
In this example, we can see that for a popular media site that the **resource load duration** is the smallest component. The real opportunities for improvement for this site lie in **TTFB** , and **resource load delay** , with a smaller opportunity in **element render delay**.
High values in each subpart is indicative of different issues:
  * High **Time to First Byte (TTFB)** usually points to server, network, or redirect issues as explained in [Optimize TTFB](https://web.dev/articles/optimize-ttfb).
  * High **resource load delay** indicates the LCP image is discovered late by the browser—for example, an LCP image that's injected by client-side JavaScript that takes a while to run.
  * High **resource load duration** is where you should look at reducing the image download size.
  * High **element render delay** is when the image is available (perhaps through a `<link rel=preload>` but not used for a long time—again often due to client-side JavaScript being required to show the image.


We hope that making this data available in CrUX at both an origin and URL-level (subject to [the usual eligibility criteria](https://developer.chrome.com/docs/crux/methodology#eligibility)) helps make it easier for sites to optimize their LCP metric.
### LCP resource types
Since the subparts are best viewed for image LCPs, CrUX restricts this data only to pages with images. Therefore, it's important to understand how many of your LCPs are image LCPs as opposed to text LCPs (such as `<h1>` headings and long paragraphs, for example).
In addition to the LCP image subparts, the CrUX APIs now also include a resource breakdown showing the split of LCP page loads between text and images.
For example, to get the LCP resource types for `https://web.dev/` for `PHONE` pageviews you can use the following curl command (again, replacing `API_KEY` with [your own key](https://developer.chrome.com/docs/crux/api#crux_api_key)):
```
curl"https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=API_KEY"\
--header'Content-Type: application/json'\
--data'{ "formFactor": "PHONE",
      "url": "https://web.dev/",
      "metrics": ["largest_contentful_paint_resource_type"]}'

```

And you'll get something like this back:
```
{
"record":{
"key":{
"formFactor":"PHONE",
"url":"https://web.dev/"
},
"metrics":{
"largest_contentful_paint_resource_type":{
"fractions":{
"image":0.0155,
"text":0.9845
}
}
},
"collectionPeriod":{
"firstDate":{
"year":2025,
"month":1,
"day":12
},
"lastDate":{
"year":2025,
"month":2,
"day":8
}
}
}
}

```

CrUX Vis has also been updated to display this data:
LCP resource types in CrUX Vis
For [web.dev's home page](https://web.dev/) for example we can see that 98.5% of LCPs were in fact text LCPs, so the LCP image subparts are less useful for this page. In that case, we can use the original TTFB and FCP metrics as a potentially better diagnostic breakdown.
LCP resource types are another useful diagnostic tool for understanding and improving LCP, especially for knowing how useful the LCP image subparts are.
## RTT diagnostic information
We have also expanded the [RTT metric first introduced in August 2024](https://developer.chrome.com/docs/crux/release-notes#202408).
### RTT tri-bins
We have added tri-bins to the CrUX APIs showing three groupings of RTT densities:
**Network Latency** | **Start** | **End**  
---|---|---  
Low | 0 milliseconds | < 75 milliseconds  
Medium | 75 milliseconds | < 275 milliseconds  
High | 275 milliseconds | ∞  
These bins are more informative than [the previous ECT categories](https://wicg.github.io/netinfo/#effective-connection-types) which included everything less than 270 milliseconds in the `4g` category. With the advances in networking technology since those were launched, most sites saw most of their traffic in that category making this categorisation less useful.
This is why we suggest using the labels **low** , **medium** , and **high** distributions rather than the usual **good** , **needs improvement** , and **poor** labels. They are not metrics a site owner can improve directly themselves, and are therefore diagnostic metrics to understand the other metrics and why they may be different than expected. They can also help explain why other metrics move over time, despite the site not changing if they show a change in the user base.
These bins are available in the CrUX APIs, for example for `web.dev` for `PHONE` pageviews (again, replacing `API_KEY` with [your own key](https://developer.chrome.com/docs/crux/api#crux_api_key)):
```
curl"https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=API_KEY"\
--header'Content-Type: application/json'\
--data'{ "formFactor": "PHONE",
      "url": "https://web.dev/",
      "metrics": ["round_trip_time"]}'

```

Which returns something like this:
```
{
"record":{
"key":{
"formFactor":"PHONE",
"url":"https://web.dev/"
},
"metrics":{
"round_trip_time":{
"histogram":[
{
"start":0,
"end":75,
"density":0.1524
},
{
"start":75,
"end":275,
"density":0.6641
},
{
"start":275,
"density":0.1835
}
],
"percentiles":{
"p75":230
}
}
},
"collectionPeriod":{
"firstDate":{
"year":2025,
"month":1,
"day":12
},
"lastDate":{
"year":2025,
"month":2,
"day":8
}
}
}
}

```

The bins are shown in CrUX Vis when **distributions** are selected:
RTT data in CrUX Vis.
### RTT in BigQuery
As well as expanding the RTT metric in the CrUX APIs to include the tri-bins, we have also made the data available in the monthly BigQuery dataset including a full histogram in 25 millisecond buckets in [the raw tables](https://developer.chrome.com/docs/crux/bigquery#schema_raw_tables) and tri-bins and p75 values in [the materialized tables](https://developer.chrome.com/docs/crux/bigquery#schema-materialized).
This allows a deeper understanding of the distribution of data beyond the tri-bins available in the CrUX APIs. It also allows us to recreate the ECT breakdown that has been removed from CrUX as of this month (more on that later)—with the slight change of a 275 millisecond threshold for `4g` instead of the previous 270 millisecond threshold. The ECT breakdowns (now sourced from RTT data) continue to be available in the [CrUX BigQuery materialized tables](https://developer.chrome.com/docs/crux/bigquery#schema-materialized) so tools like the [CrUX Dashboard](https://developer.chrome.com/docs/crux/dashboard) can continue to show this breakdown.
The BigQuery dataset also includes data by [country](https://developer.chrome.com/docs/crux/methodology/dimensions#country-dimension) (as defined by [ISO 3166-1](https://www.wikipedia.org/wiki/ISO_3166-1_alpha-2)). This allows deeper analysis which can be useful to explain why performance metrics are worse for some users. For example, we can look at the data for Google Phone users by looking at the data for `https://www.google.com`:
```
SELECT
`chrome-ux-report`.experimental.GET_COUNTRY(country_code)ASgeo,
least(500,p75_rtt)AScapped_p75_rtt,
p75_rtt
FROM
`chrome-ux-report.materialized.country_summary`
WHERE
origin='https://www.google.com'AND
yyyymm=202501AND
device='phone'
ORDERBY
p75_rttDESC,
country_code

```

Then we visualize the data on a Geo map:
75th percentile Phone RTT by country for `https://www.google.com`([source data with interactive chart](https://docs.google.com/spreadsheets/d/1VNKRpokBWQi-Hzx4MS3g0jtkDVx7m8_3-SzWhVCrH6Q/edit?pli=1&gid=0#gid=0)).
We can see that, while most of the world (particularly the "Western world") has very good RTTs, Sub-Saharan Africa, parts of the Middle East, and parts of Asia struggle more. In fact the graph is capped at 500 milliseconds RTT as using the full data skewed the colors—especially with Eritrea at a 75th percentile of 3,850 milliseconds!
This can also be useful when traffic patterns change. For example a greater proportion of users from those countries with higher RTTs may explain worse Core Web Vitals stats despite the site not changing anything.
While sites can't directly improve RTT, making this data available by a site's visitors allows for a better understanding of your site's users across the globe. It also raises lots of opportunities for analysis in future and we hope researchers will find interesting insights from this dataset.
## Removal of the ECT dimension
The final change in the February 2025 release is the retirement of the Effective Connection Type (ECT) dimension from BigQuery (we had already [removed RTT from the APIs from September 2024](https://developer.chrome.com/docs/crux/release-notes#202408) when we introduced the RTT metric as its replacement then).
As mentioned previously in this post, the RTT metric allows a more fine-grained view of connection details of a site's visitors. You can even recreate the ECT buckets from those histograms. (Technically, [ECT should be a combination of RTT and downlink speed](https://wicg.github.io/netinfo/#effective-connection-types), but [Chrome only ever used RTT](https://chromium-review.googlesource.com/c/chromium/src/+/1469649).)
An important difference is that ECT was a [CrUX dimension](https://developer.chrome.com/docs/crux/methodology/dimensions)—meaning the other metrics could be segmented by ECT. RTT is a [CrUX metric](https://developer.chrome.com/docs/crux/methodology/metrics) instead of a dimension, so it's not possible to view LCP by RTT for example, but only to see the RTTs by the other dimensions (device type and country).
This may sound more limiting, but the move from dimension to metric actually unlocks more data in CrUX. This is because CrUX has certain minimum thresholds before we are able to show data. We already [made dimensions optional in 2022](https://developer.chrome.com/docs/crux/release-notes#202205) meaning we removed ECT, or device where necessary to report at a higher level, but metrics that were not on most page loads ([Interaction to Next Paint (INP)](https://web.dev/articles/inp), different navigation types, and now LCP image subparts) were frequently not available for origins in BigQuery.
By reducing the number of dimensions, the data is less segmented, so the number of origins meeting these minimum requirements is increased. In January, we report INP for 68.1% of origins, whereas for the December dataset, we reported INP only for 64.5% of origins. The mechanism applies also to Navigation Types, the LCP Subparts and Resource Types in this release—they all benefit from the removal of the ECT dimension. In the CrUX APIs, the increased coverage has taken effect from the beginning of February.
The ECT columns will remain in BigQuery for consistency with previous datasets, and the ECT data in the materialized views will remain available, but based on the RTT information (with a 5 millisecond difference for `3g` and `4g` as noted previously) in addition to the new RTT p75 and tri-bins.
## Conclusion
The addition of more metrics to the public CrUX dataset gives site owners and researchers a lot more information to help diagnose and ultimately fix performance issues.
As a public dataset, CrUX has certain limitations to the level of detail we can show—for example, individual element selectors will never be able to be shown in CrUX. Site owners seeking this level of detail are strongly advised to implement a RUM solution, which won't be as constrained.
However, higher-level aggregated data such as those detailed in this post, can help bridge the gap between knowing you have a problem and why the problem exists. We hope this extra data will prove useful. Do [let us know on the discussion group](https://groups.google.com/a/chromium.org/g/chrome-ux-report) if you have any feedback or questions!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-02-11 UTC.

