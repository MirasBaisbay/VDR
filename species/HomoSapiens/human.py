import requests
import json
from typing import List, Dict

def query_pdb_structures(query: Dict) -> List[str]:
    base_url = "https://search.rcsb.org/rcsbsearch/v2/query?json="
    
    try:
        # Make a direct POST request with the JSON data
        response = requests.post(base_url, json=query, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if "result_set" in data:
            results = []
            for entry in data["result_set"]:
                results.append({
                    "pdb_id": entry["identifier"],
                    "score": entry.get("score", "N/A")
                })
            return results
        else:
            print("No results found in response")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return []

# Your predefined list of allowed PDB IDs
allowed_pdb_ids = ['1db1', '1ie8', '1ie9', '1rjk', '1rk3', '1rkg', '1rkh', '1s0z', '1s19', '1txi', '2ham', '2har', '2has', '2hb7', '2hb8', '2hbh', '2hc4', '2hcd', '2o4j', '2o4r', '2zfx', '2zl9', '2zla', '2zlc', '2zmh', '2zmi', '2zmj', '2zxm', '2zxn', '3a2h', '3a2i', '3a2j', '3a3z', '3a40', '3a78', '3afr', '3aun', '3auq', '3aur', '3ax8', '3az1', '3az2', '3az3', '3b0t', '3cs4', '3cs6', '3dr1', '3kpz', '3m7r', '3o1d', '3o1e', '3ogt', '3p8x', '3tkc', '3vhw', '3vjs', '3vjt', '3vrt', '3vru', '3vrv', '3vrw', '3vt3', '3vt4', '3vt5', '3vt6', '3vt7', '3vt8', '3vt9', '3vtb', '3vtc', '3vtd', '3w0a', '3w0c', '3w0g', '3w0h', '3w0i', '3w0j', '3w0y', '3w5p', '3w5q', '3w5r', '3w5t', '3wgp', '3wt5', '3wt6', '3wt7', '3wtq', '3wwr', '3x31', '3x36', '4fhh', '4fhi', '4g1d', '4g1y', '4g1z', '4g20', '4g21', '4g2h', '4g2i', '4ia1', '4ia2', '4ia3', '4ia7', '4ite', '4itf', '4q0a', '4ruj', '4ruo', '4rup', '4ynk', '5awj', '5awk', '5b41', '5b5b', '5e7v', '5gic', '5gid', '5gie', '5gt4', '5h1e', '5lga', '5mx7', '5nky', '5nma', '5nmb', '5ow7', '5ow9', '5owd', '5v39', '5xpl', '5xpm', '5xpn', '5xpo', '5xpp', '5xuq', '5xzf', '5xzh', '5ysy', '5yt2', '5zwe', '5zwf', '5zwh', '5zwi', '6fo7', '6fo8', '6fo9', '6fob', '6fod', '6jez', '6k5o', '6t2m', '6xzh', '6xzi', '6xzj', '6xzk', '6xzv', '7b39', '7bns', '7bnu', '7bo6', '7c7v', '7c7w', '7oxu', '7oxz', '7oy4', '7qpi', '7qpp', '7vqp', '7zfg', '7zfx', '8ck5', '8ckc', '8iqn', '8iqt', '8p9w', '8p9x', '8pwd', '8pwe', '8pwf', '8pwm', '8pz6', '8pz7', '8pz8', '8pz9', '8pzb', '9eyr', '9ez1', '9ez2', '9fbf', '9gy8', '9gya', '9gyc', '9gyj', '9gyk']

# Your existing query
query = {
  "query": {
    "type": "group",
    "nodes": [
      {
        "type": "terminal",
        "service": "full_text",
        "parameters": {
          "value": "VDR"
        }
      },
      {
        "type": "group",
        "nodes": [
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "rcsb_entity_source_organism.ncbi_scientific_name",
              "value": "Homo sapiens",
              "operator": "exact_match"
            }
          }
        ],
        "logical_operator": "or",
        "label": "rcsb_entity_source_organism.ncbi_scientific_name"
      }
    ],
    "logical_operator": "and"
  },
  "return_type": "entry",
  "request_options": {
    "paginate": {
      "start": 0,
      "rows": 200
    },
    "results_content_type": [
      "experimental"
    ],
    "sort": [
      {
        "sort_by": "score",
        "direction": "desc"
      }
    ],
    "scoring_strategy": "combined"
  }
}

# Execute the query
all_results = query_pdb_structures(query)

# Filter results to only include the allowed PDB IDs (case-insensitive comparison)
filtered_results = [result for result in all_results if result['pdb_id'].lower() in allowed_pdb_ids]
pdb_ids = []

# Print filtered results in a formatted way
if filtered_results:
    print("\nFound structures (filtered):")
    for result in filtered_results:
        print(f"PDB ID: {result['pdb_id']}, Score: {result['score']}")
        pdb_ids.append(result['pdb_id'])
    print(f"\nTotal filtered structures found: {len(filtered_results)}")
    print(pdb_ids)
else:
    print("No structures found after filtering.")