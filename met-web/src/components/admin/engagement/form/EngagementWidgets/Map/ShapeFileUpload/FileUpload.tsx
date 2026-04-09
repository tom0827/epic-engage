import React from 'react';
import { FileUploadContextProvider } from './FileUploadContext';
import Uploader from './Uploader';
import { Accept } from 'react-dropzone';

interface UploaderProps {
    handleAddFile: (_files: File[]) => Promise<boolean>;
    savedFile?: File;
    savedFileName?: string;
    acceptedFormat?: Accept;
}

export const FileUpload = ({ handleAddFile, savedFileName = '', acceptedFormat }: UploaderProps) => {
    return (
        <FileUploadContextProvider handleAddFile={handleAddFile} savedFileName={savedFileName}>
            <Uploader acceptedFormat={acceptedFormat} />
        </FileUploadContextProvider>
    );
};

export default FileUpload;
