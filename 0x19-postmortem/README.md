TITLE: 0x19. Postmortem
Postmortem Analysis and Action Plan for web Application Outage:

ISSUE SUMMARY;
Duration: The problem started at 10:00 AM and lasted until 12:30 PM, all times in GMT (Greenwich Mean Time).

Impact: Mainly our web application.

How bad was it? The performance of the web application slowed down by half (50%) for some users, and about a quarter (25%) of users experienced the application being unavailable at times.
Why did it happen? Our traffic distribution system (load balancer) was not set up correctly. This caused too much traffic to go to some servers, overloading them.

TIMELINE:
Friday, 10:00 AM: We got an alert that our servers were taking longer than usual to respond.
10:05 AM: We let the engineers know there might be a problem.
10:10 AM: The engineers started looking into what was causing the slowness. They checked the health of the servers and how much data was flowing through the network.
10:30 AM: At first, they thought the database might be overloaded, so they increased its resources.
11:00 AM: They then checked the settings for the load balancer (a device that distributes traffic between servers) in case it wasn't working right.
11:30 AM: Since the problem wasn't solved yet, they called in more experienced engineers and the team that manages the servers (DevOps team) to help investigate further.
12:00 PM: By looking at the logs from the load balancer, they confirmed that its settings were messed up.
12:30 PM: They fixed the settings, and everything went back to normal.

ROOT CAUSE AND SOLUTION:
The problem was that the traffic balancer, which is supposed to spread work evenly between the servers, wasn't set up correctly. This meant some servers were overloaded with work while others were barely doing anything. As a result, the website slowed down and sometimes even went down completely.

We fixed the issue by checking the traffic balancer settings and making sure it sends work to all the servers equally. We also adjusted the monitoring system to warn us if something like this happens again.
CORRECTIVE AND PREVENTATIVE MEASURES:
1. Regularly Check Your Load Balancer Settings:
It's important to take a close look at how your load balancer is configured every now and then. This helps prevent mistakes that could cause problems later.
2. Set Up Automatic Alerts:
Imagine a system that automatically tells you if something strange happens with your traffic or if the load balancer settings aren't working right. That's what these "automated monitoring alerts" do!

3. Test How Your System Handles Heavy Traffic:
We should regularly test how well our system can handle a lot of users at once. This helps us make sure it won't crash or slow down if things get busy.
4. Keep Your Load Balancer Documents Updated:
Imagine a guide on how to use the load balancer the right way. We should update these documents whenever things change to make sure everyone knows the best practices.
5. Train Your Team on Load Balancers:
It's important for the engineers working on the system to understand how the load balancer works and how to fix problems if they occur. We can do this by providing training sessions.

TASKS TO ADDRESS THE ISSUE:
Encourage people to share their ideas: This helps everyone learn and improve.
Regularly look back at what worked and what didn't: This way, you can avoid mistakes and build on successes.
Invest in making things stronger and more dependable: This ensures things run smoothly and don't break easily.

