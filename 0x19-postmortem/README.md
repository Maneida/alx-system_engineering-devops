# POSTMORTEM

## Issue Summary

**Duration:** August 10, 2023, 14:00 - August 11, 2023, 02:30 (UTC)

**Impact:** 35% of users faced slow website and occasional downtime due to a sudden surge in traffic from a marketing campaign.

## Root Cause

The website crashed because a marketing campaign brought in more visitors than expected, overwhelming the servers.

## Timeline

- **Aug 10, 14:00 (UTC):** Noticed slow site; thought it was routine.
- **Aug 10, 15:30 (UTC):** Assumed server load; tweaked settings.
- **Aug 10, 20:45 (UTC):** Sought help for network issue.
- **Aug 11, 01:00 (UTC):** Realized traffic spike, removed campaign.
- **Aug 11, 02:30 (UTC):** Fixed as campaign ended, site got better.

## Resolution

Taking down the marketing campaign reduced traffic, letting the site recover.

## Steps to Learn

**Campaign Testing:** Test campaigns' potential load.

**Monitoring:** Set alerts for site slowdowns.

**Traffic Handling:** Learn to manage unexpected traffic spikes.

## To-Do

- Test campaigns on a small scale first.
- Set up alerts for unusual site behavior.
- Study how to handle sudden traffic surges.
- Basically, the site crashed due to unanticipated traffic from a marketing campaign.
- Removing the campaign brought the site back up.
- Lessons include testing campaigns, monitoring, and handling traffic spikes.
