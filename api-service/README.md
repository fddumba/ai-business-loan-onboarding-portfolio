# FastAPI Integration Service Prototype

This folder contains a prototype API service for the AI Business Loan Onboarding Portfolio project.

## Purpose

The service acts as a bridge between AI extraction output and Camunda workflow variables.

It receives structured AI extraction JSON, validates the fields, maps `workflow_signal` to `verificationRoute`, and returns clean variables that can be passed into Camunda.

## Design principle

AI extracts. Workflow decides. Human reviews.

## Endpoint

```text
POST /map-to-camunda-variables# FastAPI Integration Service Prototype

This folder contains a prototype API service for the AI Business Loan Onboarding Portfolio project.

## Purpose

The service acts as a bridge between AI extraction output and Camunda workflow variables.

It receives structured AI extraction JSON, validates the fields, maps `workflow_signal` to `verificationRoute`, and returns clean variables that can be passed into Camunda.

## Design principle

AI extracts. Workflow decides. Human reviews.

## Endpoint

```text
POST /map-to-camunda-variables