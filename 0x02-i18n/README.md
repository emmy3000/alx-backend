# 0x02. i18n - Internationalization

## Introduction

Internationalization (i18n) is the process of making your web application accessible to users from different regions and languages. This documentation will guide you through the steps to implement i18n in your Flask application. You will learn how to parametrize Flask templates for displaying different languages, infer the correct locale based on various factors, and localize timestamps.

### Table of Contents
1. [Parametrizing Flask Templates](#parametrizing-flask-templates)
2. [Infer Locale](#infer-locale)
3. [Localizing Timestamps](#localizing-timestamps)
4. [Author](#author)

## 1. Parametrizing Flask Templates

Flask allows you to easily parametrize templates to display content in different languages. Follow these steps to achieve this:
   
- Create separate HTML templates for each language you want to support.
- Use Flask's `gettext` or `Babel` extensions for internationalization to handle translations.
- Pass the user's selected language preference to the template context and use it to render the appropriate template.

Example:

```python
@app.route('/')
def home():
    user_language = get_user_language()  # Implement your language selection logic here
    return render_template(f'home_{user_language}.html')
```

## 2. Infer Locale
Infer the correct locale based on URL parameters, user settings, or request headers. This ensures that your application displays content in the user's preferred language. Consider the following techniques:

- Parse the language from URL parameters, such as example.com/en for English.
- Use browser headers (Accept-Language) to determine the user's preferred language.
- Allow users to set their preferred language in their account settings.

Example:

```python
def get_user_language():
    # Implement logic to determine user's preferred language
    # You can check URL parameters, request headers, or user settings
    # Return the appropriate language code (e.g., 'en' for English)
```

## 3. Localizing Timestamps
Localizing timestamps is essential for providing a user-friendly experience. Follow these steps to localize timestamps in your Flask application:

- Use Flask-Babel or similar extensions to format timestamps according to the user's selected locale.
- Store timestamps in a consistent format (e.g., UTC) and convert them to the user's local time zone when rendering.

Example:

```python
from flask_babel import format_datetime

@app.route('/event/<event_id>')
def event_details(event_id):
    event = get_event(event_id)  # Retrieve event information
    event_time = event.start_time
    localized_time = format_datetime(event_time, format='medium')
    return render_template('event_details.html', event=event, localized_time=localized_time)
```
That's it! With these steps, you can easily implement internationalization in your Flask application and provide a seamless multilingual experience for your users.

## 4. Author
Emeka Emodi
