---
layout: page
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
title: "Committee members, helpers and CRUK representatives past and present"
meta_title: "Committee members, helpers and CRUK representatives"
permalink: "/about/committee"
---

## {{ site.data.sbd_details.year }} committee, treasurer and Cancer Research UK representatives

{% for member in site.data.committee.current -%}
- {{ member.name }}{% if member.role %} ({{ member.role }}){% endif %}
{% endfor %}

## Past committee members and Cancer Research UK representatives

{% for member in site.data.committee.past -%}
- {{ member.name }}{% if member.role %} ({{ member.role }}){% endif %}
{% endfor %}

## Committee Helpers

{% for member in site.data.committee.helpers -%}
- {{ member.name }}{% if member.role %} ({{ member.role }}){% endif %}
{% endfor %}
