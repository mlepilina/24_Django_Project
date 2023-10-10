from rest_framework.validators import ValidationError


class LinkValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            field_value = value.get(field, None)
            if field_value:
                self.find_youtube_link(field_value)

    def find_youtube_link(self, value):
        parts = value.split(' ')
        for part in parts:
            is_link = self.detect_link(part)
            if is_link and 'youtube.com' not in part:
                raise ValidationError("Невозможность прикрепить ссылку на сторонний ресурс, кроме youtube.com")

    def detect_link(self, value) -> bool:
        start_link = ['http://', 'https://']
        for start in start_link:
            if value.startswith(start):
                return True
        return False
