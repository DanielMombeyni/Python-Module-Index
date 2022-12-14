# bandclass/__main__.py

import sys
from .student import search_students
# .student dose not exit

student_name = sys.argv[2] if len(sys.argv) >= 2 else ''
print(f'Found student: {search_students(student_name)}')
