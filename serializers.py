import json


class CourseSerializer:
    """
    Serializes and deserializes Course objects to and from JSON format.
    """

    def __init__(self, course):
        self.course = course

    def to_json(self):
        """
        Returns a JSON representation of the Course object.

        Returns:
            str: A JSON-formatted string representing the Course object.
        """
        return json.dumps({
            "id": self.course.id,
            "name": self.course.name,
            "description": self.course.description,
            # Add other relevant attributes to the dictionary
        })

    @classmethod
    def from_json(cls, json_data):
        """
        Creates a Course object from a JSON-formatted string.

        Args:
            json_data (str): A JSON-formatted string representing a Course object.

        Returns:
            Course: A new Course object populated with data from the JSON string.
        """
        data = json.loads(json_data)
        return CourseSerializer(
            id=data.get("id"),
            name=data.get("name"),
            description=data.get("description"),

            # Add other relevant attributes and logic for initialization
        )

# ... Implement similar serializers for other models (e.g., ExamSerializer, StudentSerializer, MarkSerializer)
