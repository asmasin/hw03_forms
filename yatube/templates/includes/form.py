{% load user_filters %}
{% for field in form %}
  <div class="form-group row my-3 p-3">
    <label for="{{ field.id_for_label }}">
      {{ field.label }}
      {% if field.field.required %}
        <span class="required text-danger">*</span>
      {% endif %}
    </label>    
    {{ field|addclass:'form-control' }}
      {% if field.help_text %}
        <small id="{{ field.id_for_label }}-help" class="form-text text-muted">
          {{ field.help_text|safe }}
        </small>
      {% endif %}
  </div>
{% endfor %}
