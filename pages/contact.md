---
layout: page
title: "Contact"
meta_title: "Contact and use our contact form"
teaser: "Get in touch with us? Use the contact form."
permalink: "/contact/"
---

<form name="contact" method="POST" action="https://formspree.io/cabbage_parsnip@hotmail.com">
	Name: <input type ="text" name="Name" placeholder="Your name" />
	Email: <input type="email" name="_replyto" placeholder="Your email" />
	Message: <textarea name="message" placeholder="Type your Message"></textarea>
	<input type="submit" value="Send" />
	<input type="hidden" name="_next" value="/thanks" />
	<input type="hidden" name="_subject" value="New contact from website!" />
	<input type="text" name="_gotcha" style="display:none" />
</form>