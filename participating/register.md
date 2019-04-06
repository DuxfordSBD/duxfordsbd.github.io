---
layout: page
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
title: "Register a team"
permalink: "/participating/register"
---

There will be 3 races on the day, two childrens races and the adult race. The first childrens race is for children aged 4 –7 or 8-11, these must have a responsible adult accompanying them througout the race. The second childrens race is for children aged 12-15, they will complete two circuits of the [childrens race route][1] and do not require an adult to run with them.   

The adults race has three categories: aged 16+, elite and veterans (55+). The elite category is new for 2019 and is for teams that have previously, or predict they will, complete the [1.4 mile race route][2] in less than 10 minutes. 

Please ensure ages on the day are [as per the rules][3]. Both races will start at the John Barleycorn with the childrens race starting at 12pm and the adults race at 1pm.
Please note places are limited and will be allocated on a first come first serve basis. Entry costs are as follows: 

 * £5.00 per team for the childrens race
 * £10.00 per team for the adults race 
 
 Cheques should be made payable to 'Duxford Charity Derby' and payment should be sent to Peter Stribling, 16 Grange Road, Duxford, CB22 4QE no later than 31st August 2019. Alternatively you can use our [CRUK fundraising page][4] to pay the entry fee, just ensure to include your team name and that the donation is for race enry in the message you provide.

<form name="register" method="POST" action="https://formspree.io/cabbage_parsnip@hotmail.com">
	<h4>Team details.</h4>
	<br />
	Team Name: <input type ="text" name="teamName" placeholder="Your team name" />
	Name (main team member): <input type ="text" name="memberOne" placeholder="Name of first team membe" />
	Name (second team member): <input type ="text" name="memberTwo" placeholder="Name of second team member" />
	Race category: <select name="category">
		<option value="child4to7">
			Childrens race - Aged 4-7 on the day of the race
		</option>
		<option value="child8to11">
			Childrens race - Aged 8-11 on the day of the race 
		</option>
		<option value="child12to15">
			Childrens race - Aged 12-15 on the day of the race
		</option>
		<option value="adults">
			Adults race - aged 16+ 
		</option>
		<option value="elite">
			Adults race - elite, for teams expecting to complete the 1.4 mile course in under 10 minutes 
		</option>
		<option value="veterans">
			Adults race - veterans, aged 55+
		</option>
	</select>
	<hr />
	<h4>Contact details. For entrants to the childrens race please give parent/guardian details.</h4>
	<br />
	Name: <input type ="text" name="contact" placeholder="Your name" />
	Address: <input type ="text" name="address" placeholder="Contact address" />
	Telephone Number: <input type ="text" name="phone" placeholder="Your telephone number" />
	Email: <input type="email" name="_replyto" placeholder="Your email" />
	Did you enter the race in 2018: <input type="checkbox" name="previousCompetitor" value="previous" />
	<br />
	<input type="submit" value="Send" />
	<input type="hidden" name="_next" value="{{ site.url | append: site.baseurl | append: '/thanks' }}" />
	<input type="hidden" name="_subject" value="Team registration from website!" />
	<input type="text" name="_gotcha" style="display:none" />
</form>
<br />

For further information if needed, please contact: [duxfordsoapboxderby@outlook.com](mailto:duxfordsoapboxderby@outlook.com)

[1]: /participating/childrens-route
[2]: /participating/adults-route 
[3]: /partcipating/rules
[4]: /donate