// Relational and Non relational databases are two methods of data storage for applications

## Relational databases(SQL databses)

- Store data in tabular format (tables) with columns(contain data attributes) and rows(contain data values) which can be linked or connected using relationships
- Used when there's;
  // clear data structure
  // relationships
  // transactions
  // joins
  // strong validation at db level

## Non-relational databases/NoSql databases

- Do not store data in tables but instead use a variety of data models for accessing and managing schema-less data like documents and key value pairs
  // schema-less data - data that is stored without the constraints that relational databases require
- Non relational dbs are used when data changes very often
- Specifically optimized for applications that;
  -> Require large data volume
  -> Low Latency
  -> Flexible data models
  // All this can be achieved by relaxing some of the data consistency restrictions of other databases

### Types of non-relational databases

1.**Key-value databases**
-> They store data as a collection of key-value pairs
-> In a pair, the key serves as a identifier
-> Both keys and values can be anything from simple objects to complex compound objects

2. **Document databases**
   -> They store data as JSON objects that are flexible, semi-structured and hierarchical in nature

{
company_name: "AnyCompany",
address: {street:"1212 Main Street", city:"Anytown"},
phone_number: "1-800-555-0101",
industry: ["food_processing", "appliances"],
type:"private",
number_of_employees: 987
}

3. **Graph databases**
   -> They are purposely built to store and navigate relationships
   -> They use nodes to store data entities and edges to store relationships between entities

## Key Differences: relational vs. non-relational databases

## Commands

**sudo -u postgres psql** - accessing PostgreSQL terminal
-> \du - checking all the users created in the system
