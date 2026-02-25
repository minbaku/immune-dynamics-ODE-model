# 📌 Quantitative Modeling of Antigen-Driven T-Cell Activation Using Ordinary Differential Equations

A minimal mechanistic ODE model simulating antigen decay and T-cell activation dynamics to demonstrate quantitative reasoning in computational immunology.

---

## Rationale 🦠🧬

The adaptive immune response is initiated when antigen-presenting cells activate T lymphocytes. The magnitude and duration of T-cell expansion depend on antigen persistence and cellular turnover rates.

This project implements a simplified mechanistic model of antigen-driven T-cell activation using ordinary differential equations (ODEs). The goal is not to replicate full immunological complexity, but to demonstrate how biological processes can be translated into quantitative dynamical systems.

---

## 🧫 Biological Assumptions

The model is based on three assumptions:
- Antigen concentration decays over time.
- T-cell activation rate is proportional to antigen concentration.
- Activated T cells undergo natural decay.
- These assumptions capture the minimal dynamics required to describe a primary immune response.

---

## 🪀 Mathematical Formulation:

The system is described by:

   𝑑𝐴/𝑑𝑡 = −𝛿𝐴

   𝑑𝑇/𝑑𝑡 = 𝛼𝐴 − 𝛽𝑇

Where:
- 𝐴(𝑡) = antigen concentration
- 𝑇(𝑡) = activated T-cell population
- 𝛼 = activation coefficient
- 𝛽 = T-cell decay rate
- 𝛿 = antigen decay rate

The system is solved numerically using SciPy's odeint.

---

## Simulation Overview

Initial conditions:
- High antigen concentration
- No pre-existing activated T cells

Simulations explore:
- Effect of antigen persistence
- Effect of activation strength
- Effect of T-cell decay rate

Time evolution of both populations is visualized.

---
## Key Observations:

🚧 WORK IN PROGRESS

---

## Significance of this Project

This repository demonstrates:
- Translation of biological processes into differential equations
- Coupled dynamical system modeling
- Parameter interpretation in biological context
- Numerical simulation using Python

It reflects foundational quantitative reasoning relevant to computational immunology and systems biology research.

---

