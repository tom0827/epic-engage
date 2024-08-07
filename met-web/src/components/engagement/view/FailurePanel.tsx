import React from 'react';
import { Grid, Stack } from '@mui/material';
import { FailurePanelProps } from './types';
import { modalStyle, PrimaryButton, SecondaryButton, MetHeader1, MetBody } from 'components/common';
import { When } from 'react-if';
import { EngagementVisibility } from 'constants/engagementVisibility';

const FailurePanel = ({ email, handleClose, tryAgain, visibility }: FailurePanelProps) => {
    return (
        <Grid
            container
            direction="row"
            justifyContent="flex-start"
            alignItems="flex-start"
            sx={{ ...modalStyle }}
            spacing={2}
        >
            <Grid item xs={12}>
                <MetHeader1 bold>We are sorry</MetHeader1>
            </Grid>
            <Grid item xs={12}>
                <MetBody>There was a problem with the email address you provided:</MetBody>
            </Grid>

            <Grid item xs={12}>
                <MetBody>{email}</MetBody>
            </Grid>
            <When condition={visibility == EngagementVisibility.Internal}>
                <Grid item xs={12}>
                    <MetBody>
                        <strong>This is an internal engagement.</strong> Make sure you are using a government email.
                    </MetBody>
                </Grid>
            </When>
            <Grid item xs={12}>
                <MetBody>Please verify your email and try again.</MetBody>
            </Grid>
            <Grid item xs={12}>
                <MetBody>
                    If this problem persists, contact{' '}
                    <a href="mailto:eao.epicsystem@gov.bc.ca">eao.epicsystem@gov.bc.ca</a>
                </MetBody>
            </Grid>
            <Grid item container xs={12} direction="row" justifyContent="flex-end" spacing={1} sx={{ mt: '1em' }}>
                <Stack direction={{ xs: 'column', sm: 'row' }} spacing={1} width="100%" justifyContent="flex-end">
                    <SecondaryButton onClick={handleClose}>Go back to Engagement</SecondaryButton>
                    <PrimaryButton onClick={tryAgain}>Try Again</PrimaryButton>
                </Stack>
            </Grid>
        </Grid>
    );
};

export default FailurePanel;
