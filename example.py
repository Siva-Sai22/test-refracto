"""
Example file with multiple code quality issues for testing the refactoring analyzer.
"""

import os
import sys
import json
import datetime
import logging
from typing import List, Dict, Optional, Tuple, Union

class UserDataProcessor:
    """Process user data with multiple violations."""

    def __init__(self, config_file: str):
        self.config_file = config_file
        self.users = []
        self.load_config()
        self.logger = logging.getLogger(__name__)

    def load_config(self):
        """Load configuration from file."""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError as e:
            print(f"Error: Config file not found: {self.config_file}")
            raise e
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in config file: {self.config_file}")
            raise e
        except Exception as e:
            print(f"Unexpected error loading config: {str(e)}")
            raise e

    # VIOLATION 1: Very long function (> 50 lines)
    def process_user_data(self, user_data: Dict, validate: bool = True, transform: bool = True,
                         save: bool = True, notify: bool = False) -> Dict:
        """
        Process user data with multiple responsibilities - this function is too long!
        Should be refactored into smaller functions.
        """
        # Start of processing
        result = {"status": "pending", "errors": []}

        # Validation section (could be its own function)
        if validate:
            if not user_data.get("id"):
                result["errors"].append("Missing user ID")
            if not user_data.get("email"):
                result["errors"].append("Missing email")
            if not user_data.get("name"):
                result["errors"].append("Missing name")
            if user_data.get("age") and (user_data["age"] < 0 or user_data["age"] > 150):
                result["errors"].append("Invalid age")
            if user_data.get("email") and "@" not in user_data["email"]:
                result["errors"].append("Invalid email format")
            if user_data.get("phone") and len(user_data["phone"]) < 10:
                result["errors"].append("Invalid phone number")

        # Transformation section (could be its own function)
        if transform and not result["errors"]:
            processed_data = user_data.copy()
            processed_data["processed_at"] = datetime.datetime.now().isoformat()
            processed_data["processed_by"] = self.config.get("processor_name", "default")

            # Normalize email
            if "email" in processed_data:
                processed_data["email"] = processed_data["email"].lower().strip()

            # Calculate age group
            if "age" in processed_data:
                age = processed_data["age"]
                if age < 18:
                    processed_data["age_group"] = "minor"
                elif age < 65:
                    processed_data["age_group"] = "adult"
                else:
                    processed_data["age_group"] = "senior"

            # Add status flags
            processed_data["is_active"] = processed_data.get("active", False)
            processed_data["is_verified"] = processed_data.get("verified", False)
            processed_data["has_subscription"] = processed_data.get("subscription", False)

            result["processed_data"] = processed_data
            result["status"] = "transformed"

        # Save section (could be its own function)
        if save and not result["errors"] and "processed_data" in result:
            try:
                # This is a very long line that exceeds 120 characters and should be broken into multiple lines for better readability
                output_file = os.path.join(self.config.get("output_dir", "./output"), f"user_{user_data.get('id', 'unknown')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, 'w') as f:
                    json.dump(result["processed_data"], f, indent=2)

                result["saved_to"] = output_file
                result["status"] = "saved"
            except Exception as e:
                result["errors"].append(f"Failed to save: {str(e)}")
                result["status"] = "error"

        # Notification section (could be its own function)
        if notify and not result["errors"] and result["status"] == "saved":
            # Another very long line that should be broken down
            notification_message = f"User {user_data.get('id')} processed successfully and saved to {result.get('saved_to', 'unknown location')} at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            print(notification_message)
            # In real code, this would send an email or notification

        # Update statistics
        self.update_statistics(result)

        return result

    # VIOLATION 2: High cyclomatic complexity
    def update_statistics(self, result: Dict):
        """Function with high cyclomatic complexity due to many conditionals."""
        status = result.get("status", "unknown")
        has_errors = len(result.get("errors", [])) > 0

        if status == "saved" and not has_errors:
            self.config["stats"]["successful"] = self.config["stats"].get("successful", 0) + 1
        elif status == "error" or has_errors:
            self.config["stats"]["failed"] = self.config["stats"].get("failed", 0) + 1
        elif status == "transformed":
            self.config["stats"]["transformed"] = self.config["stats"].get("transformed", 0) + 1
        elif status == "pending":
            self.config["stats"]["pending"] = self.config["stats"].get("pending", 0) + 1
        else:
            self.config["stats"]["unknown"] = self.config["stats"].get("unknown", 0) + 1

        # More complex logic
        if result.get("processed_data"):
            user_data = result["processed_data"]
            if user_data.get("age_group"):
                if user_data["age_group"] == "minor":
                    self.config["stats"]["minors"] = self.config["stats"].get("minors", 0) + 1
                elif user_data["age_group"] == "adult":
                    self.config["stats"]["adults"] = self.config["stats"].get("adults", 0) + 1
                elif user_data["age_group"] == "senior":
                    self.config["stats"]["seniors"] = self.config["stats"].get("seniors", 0) + 1

            if user_data.get("is_active"):
                self.config["stats"]["active_users"] = self.config["stats"].get("active_users", 0) + 1

            if user_data.get("is_verified"):
                self.config["stats"]["verified_users"] = self.config["stats"].get("verified_users", 0) + 1

    # VIOLATION 3: Duplicate code (similar to load_config)
    def load_users_from_file(self, file_path: str):
        """Load users from file - duplicate error handling pattern."""
        try:
            with open(file_path, 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError as e:
            print(f"Error: Users file not found: {file_path}")
            raise e
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in users file: {file_path}")
            raise e
        except Exception as e:
            print(f"Unexpected error loading users: {str(e)}")
            raise e

    # Duplicate code pattern again
    def save_users_to_file(self, file_path: str):
        """Save users to file - same error handling pattern."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            print(f"Error saving users: {str(e)}")
            raise e

# VIOLATION 4: Another long function
def complex_calculation(a: int, b: int, c: int, operation: str = "sum") -> Union[int, float]:
    """Perform complex calculation with many branches."""
    result = 0

    if operation == "sum":
        result = a + b + c
    elif operation == "product":
        result = a * b * c
    elif operation == "average":
        result = (a + b + c) / 3
    elif operation == "min":
        result = min(a, b, c)
    elif operation == "max":
        result = max(a, b, c)
    elif operation == "sqrt_sum":
        result = (a**0.5) + (b**0.5) + (c**0.5)
    elif operation == "log_sum":
        import math
        if a > 0 and b > 0 and c > 0:
            result = math.log(a) + math.log(b) + math.log(c)
        else:
            result = -1
    elif operation == "weighted_average":
        weights = [0.3, 0.4, 0.3]
        result = (a * weights[0]) + (b * weights[1]) + (c * weights[2])
    elif operation == "geometric_mean":
        if a > 0 and b > 0 and c > 0:
            result = (a * b * c) ** (1/3)
        else:
            result = -1
    elif operation == "harmonic_mean":
        if a != 0 and b != 0 and c != 0:
            result = 3 / ((1/a) + (1/b) + (1/c))
        else:
            result = -1
    else:
        result = a + b - c

    # Post-processing
    if result > 1000:
        result = result / 1000
    elif result < 0:
        result = abs(result)

    # Format based on type
    if isinstance(result, float):
        result = round(result, 2)

    return result

# VIOLATION 5: Function with too many parameters
def create_user_report(user_id: int, user_name: str, user_email: str, user_age: int,
                       user_address: str, user_phone: str, user_status: str,
                       user_role: str, registration_date: datetime.datetime,
                       last_login: datetime.datetime, login_count: int,
                       total_purchases: float, is_premium: bool,
                       newsletter_subscribed: bool, marketing_opt_in: bool) -> Dict:
    """Function with too many parameters - should use a data class or dictionary."""
    return {
        "id": user_id,
        "name": user_name,
        "email": user_email,
        "age": user_age,
        "address": user_address,
        "phone": user_phone,
        "status": user_status,
        "role": user_role,
        "registration_date": registration_date.isoformat(),
        "last_login": last_login.isoformat() if last_login else None,
        "login_count": login_count,
        "total_purchases": total_purchases,
        "is_premium": is_premium,
        "newsletter_subscribed": newsletter_subscribed,
        "marketing_opt_in": marketing_opt_in
    }

# This line is intentionally very long to trigger the line length check - it exceeds 120 characters and should be broken into multiple lines for better readability and maintainability in the codebase
print(f"Initializing user data processor with config: {json.dumps({'output_dir': './output', 'processor_name': 'default', 'stats': {'successful': 0, 'failed': 0}}, indent=2)}")

if __name__ == "__main__":
    # Example usage
    processor = UserDataProcessor("config.json")

    # Create test data
    test_user = {
        "id": 123,
        "name": "John Doe",
        "email": "JOHN.DOE@EXAMPLE.COM",
        "age": 30,
        "phone": "1234567890",
        "active": True,
        "verified": True,
        "subscription": True
    }

    # Process the user
    result = processor.process_user_data(test_user, notify=True)
    print(f"Result: {json.dumps(result, indent=2)}")

    # Test complex calculation
    calc_result = complex_calculation(10, 20, 30, "weighted_average")
    print(f"Calculation result: {calc_result}")

    # This is another very long line that should be broken down into multiple lines for better readability in the code editor
    report = create_user_report(1, "Alice", "alice@example.com", 25, "123 Main St", "555-0123", "active", "user", datetime.datetime.now(), datetime.datetime.now(), 42, 999.99, True, True, False)
    print(f"Report created for user ID: {report['id']}")
