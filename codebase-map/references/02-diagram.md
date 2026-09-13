# Evidence-backed diagrams

## Define the question

Choose the view that answers the request: system context, component dependencies, request sequence, deployment, or data lifecycle. Avoid combining these into an unreadable graph. Use the user's format; otherwise prefer Mermaid for compact versionable diagrams and `.drawio` when editable layout matters.

## Establish nodes and edges

Identify every node by a real module, service, database, or external interface. For each edge record its meaning and source evidence: import, call, event, queue, ownership, or configured deployment link. Keep the evidence in a short caption/table or source comments. Distinguish synchronous calls, asynchronous events, and storage access when the distinction matters.

Mark a justified inference explicitly; omit unsupported topology. A node may be external or unavailable, but label that limitation. Do not turn directories into microservices or label a configured service as observed live.

## Build and verify

- Group by feature or runtime boundary; use consistent labels and a clear reading direction. Split a crowded graph into overview/detail views rather than forcing an arbitrary node count.
- Mermaid: use ordinary supported syntax for the selected renderer, quote labels with punctuation, escape special characters, and check with an available renderer/parser. If no renderer is available, state syntax was only inspected.
- draw.io: emit valid `mxfile`/`mxGraphModel` XML with unique IDs, real edge endpoints, vertex geometry, and XML-escaped labels. Parse the XML locally; rendering/opening it is a separate visual check.
- Inspect the rendered diagram when available for clipped labels, crossing edges, missing arrowheads, and contrast. A parse success does not establish visual quality.

Save to the user's requested destination or established docs area. Deliver the source artifact and any useful preview. Do not paste large XML into chat or modify unrelated architecture docs merely to host the diagram.
