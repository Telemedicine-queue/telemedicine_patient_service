# 🧑‍⚕️ Patient Service

## Overview

The **Patient Service** manages all patient-related data and operations within the distributed telemedicine system.  
It is responsible for handling **patient identities**, maintaining **patient records**, and initiating **appointment requests**.

This service is designed as an **independent, state-owning microservice**, following distributed systems best practices.

---

## Responsibilities

- Register and manage patient records  
- Retrieve patient information  
- Forward appointment requests to the **Queue Service**  

---

## Why a Separate Microservice?

From a **Distributed Systems perspective**:

- Patient data has a **distinct lifecycle**
- Independent scaling is required for varying patient load
- Strong isolation improves **reliability** and **security**

This design avoids:
- Shared databases  
- Tight coupling between services  

---

## Database Ownership

- Owns its **private database**
- No other service accesses patient data directly
- All access occurs via **exposed APIs**

This follows the **database-per-service principle**, ensuring:
- Data integrity  
- Failure isolation  
- Independent schema evolution  

---

## Integration & Communication

### 🔹 Synchronous Communication (RPC)

- Communicates with the **Queue Service** to initiate appointment requests  
- Accessed by the **API Gateway** for client-facing operations  

### 🔹 Transparency

- Clients are unaware of the service’s physical location  
- Demonstrates **location transparency**

---

## Distributed Systems Concepts Demonstrated

- Access transparency  
- Location transparency  
- Stateless service interaction  
- Failure containment  
- Data ownership and encapsulation  

---

## Failure Handling

- Patient data remains accessible even if the **Queue Service** is unavailable  
- Requests can be retried safely without data inconsistency  
- No cascading failures to other services  

---

## Key Takeaway

The **Patient Service** illustrates **independent state management** and clean service boundaries — a core principle of scalable and reliable distributed systems.

---

## Project Setup

### Requirements

- Python 3.11+
- See `requirements.txt`

### Quick Start (Windows CMD)

```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
