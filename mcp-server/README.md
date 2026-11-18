# Nimbus Campus Helpdesk – MCP Server

Official Model Context Protocol (MCP) server for the Nimbus University Helpdesk agent.
Exposes tools for academic timetable queries, student fee status reconciliation, and residential hostel rules.

## Capabilities

| Capability | Name / URI | Type | Description |
|---|---|---|---|
| Tool | `get_timetable(batch, day)` | Tool | Queries class schedules from `data/timetable.csv`. |
| Tool | `get_fee_status(student_id)` | Tool | Queries financial reconciliation from `data/fees.json`. |
| Resource | `hostel://rules` | Resource | Exposes residential rules from `data/hostel-rules.md`. |

## Requirements & Setup

1. **Python Environment**:
   - Python 3.10+ (tested on Python 3.14).
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Server Directly**:
   ```bash
   python server.py
   ```
   The server listens over standard input/output (`stdio`) using JSON-RPC 2.0.

3. **Running Automated Tests**:
   ```bash
   pytest tests/test_server.py -v
   ```

4. **MCP Inspector / Debugging**:
   To test with the interactive official MCP Inspector:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

## JSON-RPC 2.0 Protocol Examples

### 1. Initialize Handshake
**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "nimbus-client", "version": "1.0.0"}
  }
}
```
**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {"listChanged": false},
      "resources": {"listChanged": false, "subscribe": false},
      "prompts": {"listChanged": false}
    },
    "serverInfo": {"name": "campus-helpdesk", "version": ""}
  }
}
```

### 2. Tools Listing (`tools/list`)
**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list",
  "params": {}
}
```

### 3. Tool Invocation (`tools/call`)
**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "get_timetable",
    "arguments": {"batch": "CSE-A", "day": "Monday"}
  }
}
```

## Security & Privacy Considerations
- **No PII Leaks**: The fee tool returns only tuition reconciliation status (`paid`, `pending`, `overdue`) without exposing bank details or national identification numbers.
- **Strict Input Validation**: Rejects invalid student formats and days before evaluating filesystem data.
- **Hallucination Prevention**: Explicitly returns an unavailable message when no matching records exist.
