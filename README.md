
### Part A: Requirement Analysis & FURPS

#### Requirement Analysis:

   - **Functionality:**
     - *Capability:* The system should support different user roles (members and librarians) with role-specific functionalities. For members, this might include searching for books, borrowing books and returning books. Librarians would need functionalities for adding new books, updating book details, and managing member information.
     - *Reusability:* Components like user authentication, book search functionality, and borrowing processes should be designed for reuse across different modules.
     - *Security:* User authentication, data encryption, and access control are essential. Sensitive data like member information and borrowing records must be securely managed.

   - **Usability:**
     - *Human Factors:* The interface should be intuitive for all user types, accommodating varied tech proficiency. It should have a responsive design for different devices.
     - *Consistency:* The system should maintain a consistent look and feel across all modules and user roles.
     - *Documentation:* Comprehensive user guides for each user role, FAQs, and system manuals are necessary.

   - **Reliability:**
     - *Availability:* The system should be available 24/7, with minimal downtime.
     - *Failure Rate & Duration:* It should have a low failure rate. Any system failures should be resolved quickly.
     - *Predictability:* System behavior in response to user actions should be predictable and consistent.

   - **Performance:**
     - *Speed:* Fast response times for user queries and actions.
     - *Efficiency:* Optimized for minimal resource consumption without compromising functionality.
     - *Resource Consumption:* Should be optimized to work smoothly on standard hardware.
     - *Scalability:* Capable of handling an increasing number of users and data volume.

   - **Supportability:**
     - *Testability:* The system should be easily testable to find and fix bugs.
     - *Extensibility:* It should be designed to allow easy updates and additions of new features.
     - *Serviceability:* Problems within the system should be easy to diagnose and fix.
     - *Configurability:* Allow easy configuration of features like user roles, permissions, and system settings.

#### Identify Components:

   - **User (Abstract Class)**
     * *Attributes:* user_id, username, password
     * *Methods:* login(), logout()

 - **Member (Inherits User)**
     * *Attributes:* name, email
    * *Methods:* search_book(title, author), borrow_book(book), return_book(book)

 - **Librarian (Inherits User)**
    * *Attributes:* None (additional to User)
    * *Methods:* add_book(book), update_book(book), delete_book(book), manage_member(member)

 - **Book**
    * *Attributes:* title, author
    * *Methods:* get_book_info()

 - **Library**
    * *Attributes:* books (list of Book objects), members (list of Member objects)
    * *Methods:* authenticate_user(username, password), search_book(title, author), add_book(book), update_book(book), borrow_book(member, book), return_book(member, book), get_member_info(member_id)

### Part B: UML Diagrams

#### Use Case Diagram:
![E-Library Use Case.drawio](https://hackmd.io/_uploads/SygJlI8WA.png)

#### Class Diagram:
![Class Diagram.drawio](https://hackmd.io/_uploads/SyZDqIL-A.png)

