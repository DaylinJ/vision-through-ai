"""Offline illustration of the prototype's Vision response-to-speech step."""


def spoken_description(payload: dict) -> str:
    responses = payload.get("responses", [])
    if not responses:
        return "No image result was returned."

    result = responses[0]
    if result.get("error"):
        return "Object recognition is unavailable."

    annotations = result.get("localizedObjectAnnotations", [])
    names = [item["name"].strip() for item in annotations
             if isinstance(item.get("name"), str) and item["name"].strip()]
    if not names:
        return "No objects were identified."
    return "I see: " + ", ".join(dict.fromkeys(names)) + "."


if __name__ == "__main__":
    examples = [
        {"responses": [{"localizedObjectAnnotations": [{"name": "Apple"}]}]},
        {"responses": [{}]},
        {"responses": [{"error": {"message": "Example error"}}]},
    ]
    for example in examples:
        print(spoken_description(example))
