# AI-Based Automatic Report & Document Generator
## For Schools & Colleges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) [![Status](https://img.shields.io/badge/Status-Development-orange)](https://github.com/)

---

## Project Overview

The **AI-Based Automatic Report & Document Generator** is an advanced system designed to automate the generation of school and college reports, documents, and certificates. Using AI, this platform enables **teachers, admins, and staff** to save time and ensure **accurate, professional, and error-free reports** for students, classes, and the entire institution.

The platform supports **role-based access**, automation, AI-powered analytics, and customizable document templates, making it **perfect for schools, colleges, and educational organizations**.

---

## Implementation Status

**Current Phase:** Pilot/MVP Development (Active)

This is a pilot project that demonstrates the core functionality of an AI-based report generation system for educational institutions. The current implementation includes:

### ✅ Implemented Features
- **Authentication System** - User login, signup, and role-based access control
- **Core Data Models** - Student, teacher, parent, and user profile management
- **CSV Data Handling** - Automated CSV file detection and data storage
- **Basic Report Generation Framework** - Foundation for attendance and marks reports
- **Modular Architecture** - Organized codebase with auth, core, model, report, dashboard, and messaging modules
- **Security Foundations** - RBAC, access logging, and encryption support

### 🚧 In Development
- **AI-powered report generation** using VIDHYA-LLM
- **Dashboard interface** for different user roles
- **Email/SMS notification system** for report distribution
- **Advanced analytics** and AI-generated insights
- **PDF/DOCX/XLSX export** functionality

### 📋 Planned (Next Versions)
- Floating overlay GUI for instant document generation
- Real-time AI suggestions for students and teachers
- Voice-activated report generation
- Analytics dashboards with AI insights
- Multi-school & multi-branch support
- Mobile application support
- Integration with LMS platforms

---

## Project Architecture

The ClassSight system is built with a modular architecture for scalability and maintainability:

### Core Modules

- **`auth/`** - Authentication & Authorization
  - `login.py` - User login and session management
  - `signup.py` - User registration
  - `roles.py` - Role-based access control (RBAC) definitions
  - `otp.py` - OTP-based verification
  - `pass.py` - Password management

- **`core/`** - Core Utilities
  - `config.py` - Configuration management
  - `csv_store.py` - CSV data storage and retrieval
  - `detect_csv_files.py` - Automated CSV file detection
  - `detect_user_type.py` - User role detection
  - `utils.py` - Utility functions

- **`model/`** - Data Models
  - `students.py` - Student data model
  - `teachers.py` - Teacher data model
  - `parents.py` - Parent/guardian data model
  - `users.py` - User profile management

- **`report/`** - Report Generation Engine
  - `attendance.py` - Attendance report generation
  - `marks.py` - Academic marks reports
  - `view_class_report.py` - Class-level analytics and reports

- **`dashboard/`** - User Dashboard Interface
  - Interactive dashboards for different user roles
  - Real-time analytics and insights

- **`messaging/`** - Communication System
  - Automated email and SMS notifications
  - Report distribution system

- **`app.py`** - Main application entry point with CLI interface

---

## Key Features

### AI-Powered Features

* **Auto-generate student report cards** - Automated creation of comprehensive student performance reports
* **AI-based performance and attendance reports** - Intelligent analysis of student attendance and academic performance
* **AI-generated teacher performance reports** - Evaluation metrics and performance summaries for educators
* **AI-powered progress summaries for students** - Personalized progress tracking and improvement suggestions
* **AI-driven lesson plan and assignment feedback suggestions** - Intelligent recommendations for curriculum enhancement
* **AI-assisted document formatting and summarization** - Automatic document styling and content summarization

### Document & Report Management

* **Auto template filling for certificates, letters, and reports** - Customizable templates with auto-population
* **Export to PDF, DOCX, XLSX** - Multiple export formats for flexibility
* **Automated email/SMS dispatch of reports** - Direct delivery to stakeholders
* **Version control & history for documents** - Track document changes and revisions
* **Role-based access control** - Secure, permission-based document access

### Data Management

* **Multi-format data support** - CSV, Excel integration for easy data import
* **Automated data validation** - Ensure data quality and consistency
* **Secure data storage** - Encrypted storage for sensitive educational data
* **Real-time data synchronization** - Up-to-date information across the system

---

## Planned Features (Next Versions)

* Floating overlay GUI for instant document generation
* Real-time AI suggestions for students and teachers
* Voice-activated report generation
* Analytics dashboards with AI insights
* Multi-school & multi-branch support
* Mobile application support
* Integration with LMS platforms

---

## VIDHYA-LLM-001 (Custom Educational LLM)

This project is powered by **VIDHYA-LLM**, a proprietary, domain-specific Large Language Model developed specifically for educational institutions.

VIDHYA-LLM is designed to understand academic structures, institutional workflows, and structured educational data, enabling accurate and reliable report and document generation for schools and colleges.

### Model Identification:

- **Model Name** - VIDHYA-LLM
- **Model Number** - VIDHYA-LLM-001
- **Zone** - public-clone-data-1
- **Version** - 1.0

### Purpose of VIDHYA-LLM-001:

VIDHYA-LLM is optimized for:
* Academic report generation
* Teacher and class-level summaries
* Structured educational content understanding
* Performance analysis and recommendations

### Model Limitations:

* VIDHYA-LLM is not a general-purpose chatbot
* Outputs depend on provided institutional data
* Final academic decisions must be validated by educators or administrators
* Model performance varies based on data quality and completeness

---

## Security & Data Protection

The project follows strict **security measures** to protect sensitive student, teacher, and institutional data. Key practices include:

* **Role-Based Access Control (RBAC)** - Limit data access by user roles
* **Encryption** - Data protection at rest and in transit
* **Access Logging** - Audit trail for all modifications and retrievals
* **Secure Communication** - Protocols for secure data exchange
* **Compliance** - Adherence to institutional policies and privacy laws

Access to restricted datasets requires formal permission. Requests are reviewed manually, and data is provided only for responsible, approved use.

For more details, see [SECURITY](Security.md).

---

## Dataset Access Policy

To ensure ethical AI usage, data privacy, and institutional compliance, most datasets used by this project are restricted and are not publicly included in this repository. Only limited sample datasets are provided for demonstration and testing purposes.

* **Total datasets:** (Prefer not to say) (restricted)
* **Public datasets:** 2–3 (included for authentication, demo, and testing)
* **Restricted datasets:** Core academic and institutional datasets

Only limited datasets are publicly available to:
* Prevent misuse of academic data
* Protect institutional privacy
* Ensure ethical AI usage

---

## Access to Restricted Datasets

Access to additional datasets is controlled and permission-based. To request extended dataset access, send an email including:

1. Organization / Institution name
2. Purpose of usage (research, deployment, contribution)
3. Data handling and security approach
4. Duration of required access

**Contact:** [📧 Request Dataset Access](mailto:jaymeenvaghela07@gmail.com?subject=Request%20for%20Access%20to%20Restricted%20VIDHYA-LLM%20Datasets&body=Dear%20Jaymeen%2C%0A%0AI%20am%20writing%20to%20formally%20request%20access%20to%20the%20restricted%20datasets%20associated%20with%20VIDHYA-LLM.%0A%0APlease%20find%20the%20required%20details%20below%3A%0A%0AOrganization%20%2F%20Institution%20Name%3A%20%0APurpose%20of%20Access%3A%20%0AIntended%20Use%20Case%3A%20%0AData%20Handling%20and%20Security%20Measures%3A%20%0ADuration%20of%20Access%20Required%3A%20%0A%0AI%20confirm%20that%20the%20datasets%20will%20be%20used%20only%20for%20the%20stated%20purpose%20and%20will%20not%20be%20shared%20or%20redistributed.%0A%0AThank%20you%20for%20your%20time%20and%20consideration.%0A%0AWarm%20regards%2C%0A%5BYour%20Full%20Name%5D%0A%5BYour%20Role%20%2F%20Title%5D%0A%5BYour%20Organization%5D)

All requests are reviewed manually, and access is granted only for valid, responsible, and compliant use cases.

---

## System Roles & Access Hierarchy

The system implements a multi-tier role-based access control structure:

- **Administrator** - Full system access, user management, and institutional settings
- **Principal/Director** - Institutional reports, staff management, policy oversight
- **Head of Department** - Department-level analytics and reporting
- **Teachers** - Student reports, attendance, and performance data for assigned classes
- **Parents** - Student progress reports and performance summaries
- **Students** - Personal performance tracking and progress reports
- **Office Staff** - Data entry, document management, and distribution

For detailed role hierarchy, see [SYSTEM_ROLES_HIERARCHY_REFERENCE.png](SYSTEM_ROLES_HIERARCHY_REFERENCE.png)

---

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- pip package manager
- CSV format data files (for sample data)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/jaymeen07-r/ClassSight-Pilot.git
   cd ClassSight-Pilot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to the main directory:
   ```bash
cd "CLASSSIGHT-PIOTS CODE"   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage Guide

### Authentication

1. **Login**: Use existing credentials
2. **Signup**: Create new account with verified email/OTP
3. **Role Assignment**: System automatically assigns role-based permissions

### Generate Reports

1. Access the dashboard appropriate for your role
2. Select report type (attendance, marks, performance, etc.)
3. Choose filters (class, date range, specific students)
4. Review generated report
5. Export to desired format (PDF, DOCX, XLSX)
6. Optionally send via email/SMS

### Data Management

1. Upload student, teacher, and attendance data via CSV
2. System validates and auto-detects file types
3. Data is securely stored with encryption
4. Access controlled via role-based permissions

---

## Technology Stack

- **Language:** Python 3.11+
- **Data Processing:** Pandas, NumPy
- **Report Generation:** Python-docx, ReportLab, openpyxl
- **Authentication:** Custom RBAC with OTP support
- **Database:** CSV-based with encryption support
- **Communication:** Email/SMS integration ready
- **Version Control:** Git & GitHub
- **CI/CD:** GitHub Actions (Node.js pipeline included)

---

## Contribution Guidelines

Contributions are welcome to improve this project in a **controlled and meaningful way**. Before contributing, please read the guidelines below carefully.

### How to Contribute

1. Fork the repository to your GitHub account
2. Create a new feature branch
   ```bash
   git checkout -b feature/short-description
   ```
3. Make your changes following the project's coding standards
4. Commit with a clear and descriptive message
   ```bash
   git commit -m "Add: brief description of the change"
   ```
5. Push the branch to your fork
   ```bash
   git push origin feature/short-description
   ```
6. Open a Pull Request with a clear explanation of:
   * What was changed
   * Why the change is needed
   * Any related issues or enhancements

### Contribution Standards

- Follow PEP 8 Python style guide
- Write clear, descriptive commit messages
- Add comments for complex logic
- Do not include sensitive data or credentials
- Ensure no breaking changes to existing functionality
- Test your changes thoroughly

---

## Documentation

- **[README.md](README.md)** - Project overview and setup guide
- **[Security.md](Security.md)** - Security policies and data protection measures
- **[DATA_PROTECTION_AND_CONFIDENTIALITY_POLICY.md](DATA_PROTECTION_AND_CONFIDENTIALITY_POLICY.md)** - Detailed data handling policies
- **[SYSTEM_ROLES_HIERARCHY_REFERENCE.png](SYSTEM_ROLES_HIERARCHY_REFERENCE.png)** - Visual role hierarchy diagram

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Contact & Support

* **Developer:** JAYMEEN N. VAGHELA
* **Email:** [jaymeenvaghela07@gmail.com](mailto:jaymeenvaghela07@gmail.com)
* **GitHub:** [github.com/jaymeen07-r](https://github.com/jaymeen07-r)

### Report Issues

For bug reports, feature requests, or general inquiries, please open an [Issue](https://github.com/jaymeen07-r/ClassSight-Pilot/issues) on GitHub.

---

## Acknowledgments

- Built as an educational technology solution for modern institutions
- Inspired by real-world challenges in academic reporting and document management
- Contributions and feedback from the education sector are welcome

---

**Last Updated:** January 2026 | **Status:** Active Development
