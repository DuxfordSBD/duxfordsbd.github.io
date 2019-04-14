---
layout: page
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
title: "Register to volunteer"
permalink: "/participating/volunteer"
---

Thank you for wanting to volunteer at this year's Soap Box Derby. Please fill in your details below and hit _Send_.

<form name="register" method="POST" action="https://formspree.io/duxfordsoapboxderby@outlook.com">
	<h3>Your details.</h3>
	Name: <input type ="text" name="contact" placeholder="Your name" required />
	Telephone Number: <input type ="text" name="phone" placeholder="Your telephone number" required />
	Email: <input type="email" name="_replyto" placeholder="Your email" required />
	How would you like to volunteer?
	<br/>
	<input type="checkbox" name="marshalling" value="marshalling">
		Marshalling the course
	<br/>
	<input type="checkbox" name="race_help" value="race_help">
		Race coordination and help
	<br/>
	<input type="checkbox" name="selling_raffle_tickets" value="selling_raffle_tickets">
		Selling raffle tickets
	<br/>
	<input type="checkbox" name="prizes" value="prizes">
		Providing raffle and auction prizes
	<br/>
	<input type="checkbox" name="auction_raffle_on_race_day" value="auction_raffle_on_race_day">
		Helping with the auction and raffle on race day
	<br/>
	<input type="checkbox" name="fundraising" value="fundraising">
		Helping to raise funds for Cancer Research UK
	<br/>
	Want to tell us about anything else: <textarea name="more_details"></textarea>
	<br />
	<input type="submit" value="Send" />
	<input type="hidden" name="_next" value="{{ site.url | append: site.baseurl | append: '/participating/volunteer_request_submitted' }}" />
	<input type="hidden" name="_subject" value="Volunteer registration from website." />
	<input type="text" name="_gotcha" style="display:none" />
</form>
<br />