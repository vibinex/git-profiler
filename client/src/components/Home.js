import React from 'react';
import { Avatar, Button, Container, withStyles } from '@material-ui/core';
import githubIcon from '../images/github-white.png';

const styles = (theme) => ({
	root: {
		marginTop: theme.spacing(8),
		justifyContent: "center",
	},
	signInButton: {
		color: 'white',
		background: 'black'
	}
})

class Home extends React.Component {
	render() {
		const { classes } = this.props;
		return (
			<Container className={ classes.root }>
				<Button
					variant="contained"
					className={ classes.signInButton }
					startIcon={ <Avatar src={ githubIcon } /> }
				>
					{/* We will probably use Passport (passportjs.org) for auth */}
					Sign In with GitHub
				</Button>
			</Container>
		)
	}
}

export default withStyles(styles)(Home);