# slack-google

Be lazy and search Google right from Slack.

Inspired from [slack-overflow](https://github.com/karan/slack-overflow) and uses [pygoogle](https://code.google.com/p/pygoogle/) for simplicity.

## Usage

From any Slack channel, just type `/google [search terms]`, and get results right there

## Integrate with your team

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/google`
  - URL: `http://rocky-thicket-8883.herokuapp.com/google`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Google search, inside Slack.`
    - Usage hint: `[search terms]`
  - Descriptive Label: `Search Google`

## Developing

```python
# Install python dependencies
$ pip install -r requirements.txt

# Start the server
$ python app.py
```
