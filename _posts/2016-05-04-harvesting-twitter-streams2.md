---
layout: article
permalink: /posts/2016-05-04-harvesting-twitter-streams2
title: "Another Try at Harvesting the Twitter Streaming API to WARC files"
author: justin_littman 
excerpt: "We'e abandoning record segmentation for harvesting the Twitter Streaming API to WARC files and trying a new approach."
---

In ["Harvesting the Twitter Streaming API to WARC files"](http://gwu-libraries.github.io/sfm-ui/posts/2015-12-15-harvesting-twitter-streams), I described an approach for recording the [Twitter Streaming API](https://dev.twitter.com/streaming/overview) in WARC files using [record segmentation](http://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.0/#record-segmentation).  The motivation for using record segmentation was that it allowed splitting up a single call to the API — a call that might have a very long duration and involve a large amount of data — into multiple WARC records spread across multiple WARC files.

* Exports seemed potentially problematic as well.  Exporting required reconstructing and reading through monster HTTP responses.  This was particularly expensive for exports that were limited to the tweets within a time period.