# Critical Infrastructure Protection – Modbus Exploitation Lab

This repository contains a technical report developed for the **Critical Infrastructure Protection** course. The project focuses on analyzing the Modbus protocol from a security perspective and performing exploitation in a controlled lab environment.

## 🧠 Objective

The goal of the lab was to simulate real-world Modbus communication between a master and a slave, then identify and exploit inherent vulnerabilities in the protocol, such as:

- Lack of authentication
- Clear-text communication
- Unrestricted register access

## 🧩 Summary of Work

- Implementation of Modbus commands in Python and execution from Kali Linux
- Writing arbitrary values to Modbus slave registers
- Capturing and analyzing Modbus packets
- Verifying integrity loss due to protocol weakness
- Discussion of the impact and mitigations

## 📄 Contents
- `docs/`
  - `practica2 PIC.pdf`: Full technical report (in Spanish), including:
    - Methodology and execution
    - Screenshots of the attacks
    - Analysis of results
    - Conclusions and reflections
  - `enunciado.pdf`: Formulation of the lab in Spanish

- `src/`: Folder with code snippets used for lab, developed using Python and Pwntools

## 🛡️ Skills Demonstrated

- Protocol-level understanding of Modbus
- Industrial cybersecurity basics
- Use of Linux tools for communication and packet inspection
- Technical documentation and structured analysis

## ⚠️ Disclaimer

This exercise was conducted in a virtualized academic environment for educational purposes only. No real industrial systems were accessed or harmed.

---

**Repository**: [mdiazbenito/Practica-Proteccion-Infraestructuras-Criticas](https://github.com/mdiazbenito/Practica-Proteccion-Infraestructuras-Criticas)
