<!--
Career Harness targeted resume template.
Target: {{ target.slug }}
Derived from: resume/master.md
Do not introduce facts absent from verified memory and the master resume.
-->

# {{ candidate.name }}

{{ target.professional_identity }}

- 연락처: {{ candidate.contact }}
- 이메일: {{ candidate.email }}
- GitHub: {{ candidate.github }}
- LinkedIn: {{ candidate.linkedin }}
- 포트폴리오: {{ candidate.portfolio }}

## Professional Summary

{{ target.summary }}

## Core Competencies

{% for group in target.competency_groups %}
- {{ group.name }}: {{ group.skills | join(", ") }}
{% endfor %}

## Experience

{% for experience in target.experience %}
### {{ experience.company }}

{{ experience.role }} · {{ experience.start }}–{{ experience.end }}

{% for bullet in experience.bullets %}
- {{ bullet.text }}
<!-- claims: {{ bullet.claim_ids | join(", ") }} -->
{% endfor %}
{% endfor %}

## Education & Activities

{% for item in target.education_and_activities %}
- {{ item.text }}
{% endfor %}
