---
layout: page
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
title: "Contact"
meta_title: "Contact and use our contact form"
teaser: "If you would like to get in touch with us you can use this contact form."
permalink: "/contact/"
---

Alternatively you can send us an email to [duxfordsoapboxderby@outlook.com](mailto:duxfordsoapboxderby@outlook.com).
<br />

<form name="contact" method="POST" action="https://formspree.io/cabbage_parsnip@hotmail.com">
	Name: <input type ="text" name="Name" placeholder="Your name" />
	Email: <input type="email" name="_replyto" placeholder="Your email" />
	Message: <textarea name="message" placeholder="Type your Message"></textarea>
	<input type="submit" value="Send" />
	<input type="hidden" name="_next" value="{{ site.url | append: site.baseurl | append: '/thanks' }}" />
	<input type="hidden" name="_subject" value="New contact from website!" />
	<input type="text" name="_gotcha" style="display:none" />
</form>

<br />
For our privacy policy see [here]({{ site.url }}{{ site.baseurl }}/privacy_policy). 