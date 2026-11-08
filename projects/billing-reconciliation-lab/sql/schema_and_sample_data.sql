-- Reproducible SQLite schema and synthetic records for the Billing Reconciliation Lab.
-- All IDs, values, and payment references are fictional.

DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS invoice_lines;
DROP TABLE IF EXISTS invoices;

CREATE TABLE invoices (
    invoice_id TEXT PRIMARY KEY,
    currency TEXT NOT NULL,
    total_minor INTEGER NOT NULL
);

CREATE TABLE invoice_lines (
    line_id TEXT PRIMARY KEY,
    invoice_id TEXT NOT NULL REFERENCES invoices(invoice_id),
    description TEXT NOT NULL,
    amount_minor INTEGER NOT NULL
);

CREATE TABLE payments (
    payment_id TEXT PRIMARY KEY,
    invoice_id TEXT NOT NULL REFERENCES invoices(invoice_id),
    provider_reference TEXT NOT NULL,
    status TEXT NOT NULL,
    amount_minor INTEGER NOT NULL
);

INSERT INTO invoices (invoice_id, currency, total_minor) VALUES
    ('INV-DEMO-1001', 'USD', 1299),
    ('INV-DEMO-1002', 'USD', 2500),
    ('INV-DEMO-1003', 'USD', 500);

INSERT INTO invoice_lines (line_id, invoice_id, description, amount_minor) VALUES
    ('LINE-1001-A', 'INV-DEMO-1001', 'Subscription', 1000),
    ('LINE-1001-B', 'INV-DEMO-1001', 'Usage', 499),
    ('LINE-1001-C', 'INV-DEMO-1001', 'Credit', -200),
    ('LINE-1002-A', 'INV-DEMO-1002', 'Subscription', 2500),
    ('LINE-1003-A', 'INV-DEMO-1003', 'Subscription', 600);

INSERT INTO payments (payment_id, invoice_id, provider_reference, status, amount_minor) VALUES
    ('PAY-1001-A', 'INV-DEMO-1001', 'REF-1001', 'succeeded', 1299),
    ('PAY-1001-B', 'INV-DEMO-1001', 'REF-1001-PENDING', 'pending', 1299),
    ('PAY-1002-A', 'INV-DEMO-1002', 'REF-DUPLICATE', 'succeeded', 1250),
    ('PAY-1002-B', 'INV-DEMO-1002', 'REF-DUPLICATE', 'succeeded', 1250),
    ('PAY-1003-A', 'INV-DEMO-1003', 'REF-1003-FAILED', 'failed', 500);
