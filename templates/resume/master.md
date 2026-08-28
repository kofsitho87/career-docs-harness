<!-- Career Harness master resume template. Replace placeholders only with verified memory. -->

# {{ candidate.name }}

{{ candidate.professional_identity }}

- 연락처: {{ candidate.contact }}
- 이메일: {{ candidate.email }}
- GitHub: {{ candidate.github }}
- LinkedIn: {{ candidate.linkedin }}
- 포트폴리오: {{ candidate.portfolio }}

## Professional Summary

{{ resume.summary }}

## Core Competencies

{% for group in resume.competency_groups %}
- {{ group.name }}: {{ group.skills | join(", ") }}
{% endfor %}

## Experience

{% for experience in resume.experience %}
### {{ experience.company }}

{{ experience.role }} · {{ experience.start }}–{{ experience.end }}

{% for project in experience.projects %}
#### {{ project.name }}

{% for bullet in project.bullets %}
- {{ bullet.text }}
<!-- claims: {{ bullet.claim_ids | join(", ") }} -->
{% endfor %}

기술: {{ project.technologies | join(", ") }}
{% endfor %}
{% endfor %}

## Education

{% for education in resume.education %}
- {{ education.school }} · {{ education.major }} · {{ education.end }}
{% endfor %}

## Open Source & Activities

{% for activity in resume.activities %}
- {{ activity.text }}
{% endfor %}
