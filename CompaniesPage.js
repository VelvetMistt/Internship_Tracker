import { Box, Button, Container, Typography } from "@mui/material";

const CompaniesPage = () => (
  <Container sx={{ p: 3 }}>
    <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center", mb: 2 }}>
      <Typography variant="h4">Company Management</Typography>
      <Button variant="contained">Add Company</Button>
    </Box>
    <Typography color="text.secondary">
      Organize company profiles, contacts, and recruiting information for every internship opportunity.
    </Typography>
  </Container>
);

export default CompaniesPage;
