# YATODO (Yet Another TODO)

## Spec

This is a simple TODO app made as an exercise in learning Django and Django-REST.

Tasks are required to have a title and optional description.

Once it is created, it can change states: 
* TODO - first state.
* STARTED - working on it.
* WAITING - waiting on the task. Someone or something is blocking.
* DONE - task is finished.
* CANCELLED - task is cancelled.

Tasks may be deleted or archived.

## Ideas

Add support for notifications, which may be scheduled for a specific
date, or categorized as "soon" or "some day".
