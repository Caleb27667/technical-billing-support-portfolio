-- SQLite investigation queries. All identifiers and values are fictional.
-- Expected tables: invoices, invoice_lines, payments.

-- 1. Compare the recorded invoice total with its line-item calculation.
SELECT i.invoice_id, i.currency, i.total_minor,
       COALESCE(SUM(l.amount_minor), 0) AS calculated_minor,
       i.total_minor - COALESCE(SUM(l.amount_minor), 0) AS difference_minor
FROM invoices AS i
LEFT JOIN invoice_lines AS l ON l.invoice_id = i.invoice_id
GROUP BY i.invoice_id, i.currency, i.total_minor
HAVING difference_minor <> 0;

-- 2. Find successful payment references used more than once.
SELECT provider_reference, COUNT(*) AS occurrences,
       SUM(amount_minor) AS total_minor
FROM payments
WHERE status = 'succeeded'
GROUP BY provider_reference
HAVING COUNT(*) > 1;

-- 3. Compare confirmed successful payments with invoice totals.
SELECT i.invoice_id, i.total_minor,
       COALESCE(SUM(CASE WHEN p.status = 'succeeded'
                         THEN p.amount_minor ELSE 0 END), 0) AS settled_minor
FROM invoices AS i
LEFT JOIN payments AS p ON p.invoice_id = i.invoice_id
GROUP BY i.invoice_id, i.total_minor
HAVING settled_minor <> i.total_minor;
