<p align="center">
  <img src="_assets/bootcamp-header.svg" alt="FastAPI Bootcamp Zero to Hero" width="800">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/weeks-16-yellow.svg" alt="16 Weeks"></a>
  <a href="#"><img src="https://img.shields.io/badge/hours-96-orange.svg" alt="96 Hours"></a>
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/🇪🇸_Español-0969DA?style=for-the-badge&logoColor=white" alt="Spanish Version"></a>
</p>

---

## 📋 Description

Intensive **16-week (~4 months)** bootcamp focused on mastering **FastAPI** and modern backend development with Python. Designed to take students from zero to **Junior Backend Developer**, with emphasis on clean code, best practices, and real-world projects.

### 🎯 Objectives

Upon completion of the bootcamp, students will be able to:

- ✅ Master Python fundamentals needed for backend development
- ✅ Build complete RESTful APIs with FastAPI
- ✅ Implement robust data validation with Pydantic v2
- ✅ Work with databases using SQLAlchemy (sync and async)
- ✅ Implement authentication and authorization (JWT, OAuth2)
- ✅ Write automated tests with pytest
- ✅ Document APIs automatically (OpenAPI/Swagger)
- ✅ Deploy applications with Docker and cloud services
- ✅ Apply clean code, design patterns, and best practices
- ✅ Build production-ready complete projects

### 🚀 Why FastAPI?

> **Modern FastAPI from day 1** - No legacy code, only current best practices.

FastAPI is Python's fastest and most modern web framework. This bootcamp focuses exclusively on FastAPI with Python 3.12+ and modern features. Students learn directly the tools and techniques they will use in the professional world.

---

## 🗓️ Bootcamp Structure

|         Stage          | Weeks | Hours | Main Topics                                            |
| :--------------------: | :---: | :---: | ------------------------------------------------------ |
| **Fundamentals**       |  1-4  |  24h  | Modern Python, async/await, FastAPI intro, Pydantic v2 |
| **Intermediate**       | 5-10  |  36h  | SQLAlchemy, CRUD, relationships, middleware, dependencies |
| **Advanced**           | 11-14 |  24h  | JWT/OAuth2, testing, WebSockets, security              |
| **Production**         | 15-16 |  12h  | Docker, CI/CD, deployment, final project               |

**Total: 16 weeks** | **96 hours** of intensive training

---

## 📚 Weekly Content

Each week includes:

```
bootcamp/week-XX/
├── README.md                 # Description and objectives
├── rubrica-evaluacion.md     # Evaluation criteria
├── 0-assets/                 # Images and diagrams
├── 1-teoria/                 # Theoretical material
├── 2-practicas/              # Guided exercises
├── 3-proyecto/               # Weekly project
├── 4-recursos/               # Additional resources
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/               # Key terms
```

### 🔑 Key Components

- 📖 **Theory**: Fundamental concepts with real-world examples
- 💻 **Practice**: Progressive exercises and hands-on projects
- 📝 **Evaluation**: Knowledge, performance, and product evidence
- 🎓 **Resources**: Glossaries, references, and supplementary material

---

## 🛠️ Tech Stack

| Technology | Version | Usage |
|------------|---------|-------|
| Python | 3.12+ | Main language |
| FastAPI | 0.115+ | Web framework |
| Pydantic | 2.x | Data validation |
| SQLAlchemy | 2.x | ORM (sync and async) |
| Alembic | 1.x | DB migrations |
| SQLite | - | Development and testing |
| PostgreSQL | 16+ | Production |
| pytest | 8+ | Testing |
| Docker | 24+ | Containerization |
| uv | latest | Package management |

**Development environment**: Docker + docker compose (❌ DO NOT install Python locally)

**API Documentation**: OpenAPI/Swagger (built into FastAPI)

---

## 🚀 Quick Start

### Prerequisites

- **Docker** and **Docker Compose** installed
- **Git** for version control
- **VS Code** (recommended) with included extensions
- Modern browser (Chrome, Firefox, Edge)

### 1. Clone the Repository

```bash
git clone https://github.com/epti-dev/bc-fastapi.git
cd bc-fastapi
```

### 2. Install VS Code Extensions

```bash
# Open in VS Code
code .

# Recommended extensions will appear automatically
# Or run: Ctrl+Shift+P → "Extensions: Show Recommended Extensions"
```

### 3. Navigate to Current Week

```bash
cd bootcamp/week-01
```

### 4. Follow Instructions

Each week contains a `README.md` with detailed instructions.

---

## 📊 Learning Methodology

### Teaching Strategies

- 🎯 **Project-Based Learning (PBL)**
- 🧩 **Deliberate Practice**
- 🔄 **API Challenges**
- 👥 **Peer Code Review**
- 🎮 **Live Coding**

### Time Distribution (6h/week)

- **Theory**: 1.5-2 hours
- **Practice**: 2.5-3 hours
- **Project**: 1.5-2 hours

### Evaluation

Each week includes three types of evidence:

1. **Knowledge 🧠** (30%): Theoretical assessments and quizzes
2. **Performance 💪** (40%): Practical exercises in class
3. **Product 📦** (30%): Evaluable deliverables (functional projects)

**Passing criteria**: Minimum 70% in each type of evidence

---

## 🤝 Contributing

Contributions are welcome! This is an open-source educational project.

### How to Contribute

1. Read the [Contributing Guide](CONTRIBUTING.md)
2. Review the [Code of Conduct](CODE_OF_CONDUCT.md)
3. Fork the repository
4. Create your branch (`git checkout -b feature/new-feature`)
5. Commit with [Conventional Commits](https://www.conventionalcommits.org/) (`git commit -m 'feat: add new exercise'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Open a Pull Request

### 📋 Contribution Areas

- ✨ Additional exercises
- 📚 Documentation improvements
- 🐛 Bug fixes
- 🎨 Visual resources (SVG diagrams)
- 🌐 Translations
- 📹 Tutorial videos

---

## 📞 Support

- 💬 **Discussions**: [GitHub Discussions](https://github.com/epti-dev/bc-fastapi/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/epti-dev/bc-fastapi/issues)

---

## 📄 License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - For creating the best Python web framework
- [Pydantic](https://docs.pydantic.dev/) - For elegant data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) - For Python's most powerful ORM
- [Sebastián Ramírez](https://github.com/tiangolo) - Creator of FastAPI
- Python Community - For resources and examples
- All contributors

---

## 📚 Additional Documentation

- [🤖 Copilot Instructions](.github/copilot-instructions.md)
- [🤝 Contributing Guide](CONTRIBUTING.md)
- [📜 Code of Conduct](CODE_OF_CONDUCT.md)
- [🔒 Security Policy](SECURITY.md)

---

<p align="center">
  <strong>🎓 FastAPI Bootcamp - Zero to Hero</strong><br>
  <em>From zero to backend developer in 4 months</em>
</p>

<p align="center">
  <a href="bootcamp/week-01">Start Week 1</a> •
  <a href="_docs">View Docs</a> •
  <a href="https://github.com/epti-dev/bc-fastapi/issues">Report Issue</a> •
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  Made with ❤️ for the developer community
</p>
