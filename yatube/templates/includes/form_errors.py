{% if form.errors %}
  {% for field in form %}
    {% for error in field.errors %}            
      <div class="alert alert-danger">
        {{ error|escape }}
      </div>
    {% endfor %}
  {% endfor %}
  {% for error in form.non_field_errors %}
    <div class="alert alert-danger">
      {{ error|escape }}
    </div>
  {% endfor %}
{% endif %}
