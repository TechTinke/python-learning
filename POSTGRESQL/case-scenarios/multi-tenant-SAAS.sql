--  Multi-Tenant SaaS Platform Isolation
-- A medical billing platform serves hundreds of independent clinics.
-- Compliance laws dictate that patient data from Clinic A must never under any circumstances be accessible to users from Clinic B, even if an application-level bug occurs. 
-- The platform must also support rapid onboarding of new clinics without taking down the system.
-- Create the database setup and ddl script

-- Schema-Per-Tenant Architecture - the database physically isolates tables into separate namespaces(schemas), preventing cross tenant access

CREATE SCHEMA tenant;

CREATE tenant.billing_ledgers(
    invoice_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id UUID NOT NULL,
    icd_10_code VARCHAR(16) NOT NULL,
    insurance_payout NUMERIC(12, 2) NOT NULL,
    patient_copay NUMERIC(12,2) NOT NULL,
    settled_at TIMESTAMPZ
);

CREATE tenant.patients(
    patient_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    national_health_id VARCHAR(64),
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESPAMPZ DEFAULT CURRENT_TIMESTAMP
);

 