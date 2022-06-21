---
layout: page
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
title: "Register a team"
permalink: "/participating/register"
---

There will be 3 races on the day, two childrens races and the adult race. The first childrens race is for children aged 4 –7 or 8-11, these must have a responsible adult accompanying them throughout the race. The second childrens race is for children aged 12-15, they will complete two circuits of the [childrens race route][1] and do not require an adult to run with them. No one over the age of 15 is allowed to be a team member in any of the children's races, and if the two team member's ages fall into two different age groups categories we would expect the team to enter into the older of the two categories. 

The adults race has three categories: aged 16+, elite and veterans (55+). The elite category was new for 2019 and is for teams that have previously, or predict they will, complete the [1.4 mile race route][2] in less than 10 minutes. Please ensure ages on the day are [as per the general rules][general_rules].

Both races will start at the John Barleycorn with the childrens race starting at 12 pm and the adults race at 1 pm.

Please note places are limited and will be allocated on a first come first serve basis. Entry costs are as follows: 

 * £5.00 per team for the childrens race
 * £10.00 per team for the adults race 


By entering you confirm that you will abide by [our general rules][general_rules] and [childrens rules][childrens_rules] or [adult rules][adults_rules], depending on which race you will compete in.

You can pay your entry fee by using our [CRUK fundraising page][4]. Just be sure to include your team name and that the donation is for race entry in the message you provide. Alternatively payment by cheque is possible. Please contact us for more information. Payment should be recieved no later than {{ site.data.sbd_details.entry_deadline }}.


<form name="register" method="POST" action="https://formspree.io/f/maylzqae">
	<h4>Team details.</h4>
	<br />
	Team Name: <input type ="text" name="teamName" placeholder="Your team name" required />
	Name (main team member): <input type ="text" name="memberOne" placeholder="Name of first team member" required />
	Name (second team member): <input type ="text" name="memberTwo" placeholder="Name of second team member" required />
	Race category: <select name="category" required>
		<option value="child4to7">
			Childrens race - Aged 4-7
		</option>
		<option value="child8to11">
			Childrens race - Aged 8-11
		</option>
		<option value="child12to15">
			Childrens race - Aged 12-15
		</option>
		<option value="adults">
			Adults race - aged 16+ 
		</option>
		<option value="elite">
			Adults race - elite, for teams expecting to complete the 1.4 mile course in under 10 minutes 
		</option>
		<option value="veterans">
			Adults race - veterans, 55+
		</option>
	</select>
	<hr />
	<h4>Contact details. For entrants to the childrens race please give parent/guardian details.</h4>
	<br />
	Name: <input type ="text" name="contact" placeholder="Your name" required />
	Address: <input type ="text" name="address" placeholder="Contact address" required />
	Telephone Number: <input type ="text" name="phone" placeholder="Your telephone number" required />
	Email: <input type="email" name="_replyto" placeholder="Your email" required />
	Did you enter the race in 2019: <input type="checkbox" name="previousCompetitor" value="previous" />
	<br />
	<p style="font-weight:bold;"> Please ensure that you include either a phone number or an email address as we will need to contact you to confirm that your entry has been sucessful.</p>
	<input type="submit" value="Send" />
	<input type="hidden" name="_next" value="{{ site.url | append: site.baseurl | append: '/participating/entry-request-submitted' }}" />
	<input type="hidden" name="_subject" value="Team registration from website." />
	<input type="text" name="_gotcha" style="display:none" />
</form>
<br />

For further information if needed, please contact: [duxfordsoapboxderby@outlook.com](mailto:duxfordsoapboxderby@outlook.com)

<br />

For our privacy policy see [here]({{ site.url }}{{ site.baseurl }}/privacy_policy). 

[1]: {{ site.url }}{{ site.baseurl }}/participating/route-map#childrens-route
[2]: {{ site.url }}{{ site.baseurl }}/participating/route-map 
[4]: {{ site.url }}{{ site.baseurl }}/participating/pay-race-entry-fee 
[general_rules]: {{site.url}}{{site.baseurl}}/participating/rules
[childrens_rules]: {{site.url}}{{site.baseurl}}/participating/childrens-rules
[adults_rules]: {{site.url}}{{site.baseurl}}/participating/adult-rules
