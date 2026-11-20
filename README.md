# Generative AI Prompt Tools

A local Python prompt-rendering example with explicit fields and input length validation. Python 3.12 and the standard library are sufficient.

## Run

```sh
python prompt.py --audience engineers --material "Example content"
```

The command prints a summarization prompt containing the requested audience and literal material. Blank inputs and inputs longer than 200 audience characters or 20,000 material characters produce argument errors. Dollar signs in material remain literal.

## Scope

The renderer prepares prompts for inspection. Model execution and output evaluation remain extension points. Material delimiters aid readability. Provider-side instructions and enforcement require separate implementation when connecting a model.
