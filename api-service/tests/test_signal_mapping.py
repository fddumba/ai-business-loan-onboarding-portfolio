from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_app_001_maps_to_request_new_document():
    payload = {
        "application_id": "APP-001",
        "document_readable": True,
        "document_type": "Utility bill",
        "company_name_extracted": "Stock Trace Limited",
        "address_extracted": "14 Market Street",
        "document_date": "2024-06-03",
        "company_name_match": True,
        "address_match": True,
        "missing_or_unclear_fields": [],
        "extraction_summary": "Old but matching document.",
        "workflow_signal": "DOCUMENT_EXPIRED_OR_WEAK",
    }

    response = client.post("/map-to-camunda-variables", json=payload)

    assert response.status_code == 200
    assert response.json()["verificationRoute"] == "REQUEST_NEW_DOCUMENT"


def test_app_002_maps_to_human_review():
    payload = {
        "application_id": "APP-002",
        "document_readable": True,
        "document_type": "Utility bill",
        "company_name_extracted": "Green Valley Trading Ltd",
        "address_extracted": "72 Industrial Way",
        "document_date": "2026-06-18",
        "company_name_match": False,
        "address_match": False,
        "missing_or_unclear_fields": [],
        "extraction_summary": "Mismatch between document and application.",
        "workflow_signal": "MISMATCH_REQUIRES_REVIEW",
    }

    response = client.post("/map-to-camunda-variables", json=payload)

    assert response.status_code == 200
    assert response.json()["verificationRoute"] == "HUMAN_REVIEW"


def test_app_003_maps_to_clean_case():
    payload = {
        "application_id": "APP-003",
        "document_readable": True,
        "document_type": "Business registration certificate",
        "company_name_extracted": "Bright Path Logistics Limited",
        "address_extracted": "22 Airport Road",
        "document_date": "2026-06-20",
        "company_name_match": True,
        "address_match": True,
        "missing_or_unclear_fields": [],
        "extraction_summary": "Evidence matches application and registry.",
        "workflow_signal": "EVIDENCE_MATCHED",
    }

    response = client.post("/map-to-camunda-variables", json=payload)

    assert response.status_code == 200
    assert response.json()["verificationRoute"] == "CLEAN_CASE"


def test_app_004_maps_to_manual_investigation():
    payload = {
        "application_id": "APP-004",
        "document_readable": True,
        "document_type": "Business registration document",
        "company_name_extracted": "Registry Issue Case",
        "address_extracted": "",
        "document_date": "2026-06-10",
        "company_name_match": False,
        "address_match": False,
        "missing_or_unclear_fields": [
            "registry_status",
            "verified_business_address",
        ],
        "extraction_summary": "Registry information is missing or unclear.",
        "workflow_signal": "REGISTRY_REQUIRES_INVESTIGATION",
    }

    response = client.post("/map-to-camunda-variables", json=payload)

    assert response.status_code == 200
    assert response.json()["verificationRoute"] == "MANUAL_INVESTIGATION"


def test_unsupported_signal_returns_400():
    payload = {
        "application_id": "APP-999",
        "document_readable": True,
        "document_type": "Unknown document",
        "company_name_extracted": "Unknown Company",
        "address_extracted": "Unknown Address",
        "document_date": "2026-06-30",
        "company_name_match": False,
        "address_match": False,
        "missing_or_unclear_fields": ["workflow_signal"],
        "extraction_summary": "Unsupported signal test.",
        "workflow_signal": "UNKNOWN_SIGNAL",
    }

    response = client.post("/map-to-camunda-variables", json=payload)

    assert response.status_code == 400
    assert "Unsupported workflow_signal" in response.json()["detail"]