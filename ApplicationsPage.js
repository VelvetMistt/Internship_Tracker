import { Box, Button, Container, Typography } from "@mui/material";

const ApplicationsPage = () => (
  <Container sx={{ p: 3 }}>
    <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center", mb: 2 }}>
      <Typography variant="h4">Internship Applications</Typography>
      <Button variant="contained">Add Application</Button>
    </Box>
    <Typography color="text.secondary">
      Manage your applications, track statuses, deadlines, and recruiter communication in one place.
    </Typography>
  </Container>
);

export default ApplicationsPage;
