# Client process flows (optional)

The build uses the standard flows from [`bpa/processes/`](../../../../bpa/processes/)
for every domain in scope. To adapt a flow for this client (extra steps, removed
branches, different lanes), **copy** the standard `*.process.json` file into this
folder and edit it — a file here with the same `domain` number overrides the standard.

Format: see [`docs/bpa.md`](../../../../docs/bpa.md#process-flow-format). Every node
with a `scenario` code becomes clickable and is colour-coded by the `Invulling` of
that scenario in `content/`.
